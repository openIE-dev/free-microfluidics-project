---
title: Browse
layout: default
nav_order: 2
permalink: /browse/
---

# Browse the corpus

Search across all 376 entries by name, prior-art notes, creator, or disclosed subsystem. Filters compose. Click any entry to expand its full record.

<style>
  .filters { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.6rem 1rem; margin: 1rem 0; }
  .filters label { display: flex; flex-direction: column; font-size: 0.85rem; opacity: 0.85; }
  .filters input, .filters select {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.15);
    color: inherit;
    padding: 0.4rem 0.5rem;
    border-radius: 4px;
    font-size: 0.95rem;
  }
  .filters input:focus, .filters select:focus { outline: 2px solid #2EE6A6; }
  #search { width: 100%; }
  #status { margin: 0.5rem 0 1rem 0; opacity: 0.7; font-size: 0.9rem; }
  .entry {
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 6px;
    padding: 0.75rem 1rem;
    margin: 0.5rem 0;
    background: rgba(255,255,255,0.02);
  }
  .entry summary { cursor: pointer; list-style: none; }
  .entry summary::-webkit-details-marker { display: none; }
  .entry-head { display: flex; justify-content: space-between; gap: 1rem; align-items: baseline; }
  .entry-name { font-weight: 600; font-size: 1.05rem; }
  .entry-year { opacity: 0.65; font-variant-numeric: tabular-nums; font-size: 0.9rem; }
  .entry-meta { font-size: 0.85rem; opacity: 0.75; margin-top: 0.2rem; }
  .badge {
    display: inline-block;
    padding: 1px 7px;
    border-radius: 3px;
    font-size: 0.75rem;
    background: rgba(255,255,255,0.08);
    margin-right: 0.4rem;
  }
  .badge.draft { background: rgba(255,170,0,0.18); }
  .badge.commons { background: rgba(46,230,166,0.18); }
  .entry-body { margin-top: 0.6rem; padding-top: 0.6rem; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.92rem; }
  .entry-body dl { display: grid; grid-template-columns: max-content 1fr; gap: 0.2rem 0.8rem; margin: 0.3rem 0 0.6rem 0; }
  .entry-body dt { opacity: 0.6; font-size: 0.85rem; }
  .entry-body dd { margin: 0; }
  .tags .tag {
    display: inline-block;
    padding: 1px 6px;
    margin: 1px 3px 1px 0;
    border-radius: 3px;
    font-size: 0.75rem;
    background: rgba(46,230,166,0.12);
    color: #2EE6A6;
    text-decoration: none;
  }
  #results { min-height: 50vh; }
</style>

<div class="filters">
  <label style="grid-column: span 3;">Search
    <input id="search" placeholder="canonical name, creator, prior art keywords, tag…" autocomplete="off">
  </label>
  <label>Corpus
    <select id="filter-corpus">
      <option value="">All</option>
      <option value="private">Private</option>
      <option value="academic">Academic</option>
      <option value="fictional">Fictional</option>
      <option value="open">Open</option>
    </select>
  </label>
  <label>IP status
    <select id="filter-ip">
      <option value="">All</option>
      <option value="patented">Patented</option>
      <option value="trade-secret">Trade secret</option>
      <option value="open-permissive">Open / permissive</option>
      <option value="public-domain">Public domain</option>
      <option value="fictional">Fictional</option>
    </select>
  </label>
  <label>Quality
    <select id="filter-quality">
      <option value="">All</option>
      <option value="commons">Commons-grade only</option>
      <option value="draft">Drafts only</option>
    </select>
  </label>
  <label>Year ≥
    <input id="filter-year-min" type="number" placeholder="1966" min="1900" max="2100">
  </label>
  <label>Year ≤
    <input id="filter-year-max" type="number" placeholder="2026" min="1900" max="2100">
  </label>
  <label>Subsystem tag (substring)
    <input id="filter-tag" placeholder="quake, droplet, herringbone, dld, …" autocomplete="off">
  </label>
</div>

<div id="status">Loading corpus…</div>
<div id="results"></div>

<script>
(async function () {
  // Pages workflow stages corpus.jsonl into /data/ at build time.
  const baseurl = "{{ site.baseurl }}";
  const url = baseurl + "/data/corpus.jsonl";
  const status = document.getElementById("status");
  const results = document.getElementById("results");

  let entries;
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(res.status + " " + res.statusText);
    const text = await res.text();
    entries = text.split("\n").filter(l => l.trim()).map(l => JSON.parse(l));
  } catch (err) {
    status.textContent = "Failed to load corpus.jsonl: " + err.message;
    return;
  }

  const $ = id => document.getElementById(id);
  const inputs = ["search", "filter-corpus", "filter-ip", "filter-quality", "filter-year-min", "filter-year-max", "filter-tag"].map($);
  inputs.forEach(el => el.addEventListener("input", render));

  function entryYear(e) {
    return parseInt((e.first_disclosure_date || "").slice(0, 4), 10) || null;
  }

  function entryHaystack(e) {
    return [
      e.canonical_name,
      (e.aliases || []).join(" "),
      e.creator,
      e.disclosure_citation,
      e.prior_art_notes,
      e.channel_geometry,
      e.fabrication_method,
      e.flow_regime,
      e.control_architecture,
      e.sensing,
      e.end_application,
      (e.notable_capabilities || []).join(" "),
      (e.disclosed_subsystems || []).join(" "),
      e.id
    ].filter(Boolean).join(" ").toLowerCase();
  }

  function matches(e) {
    const q = $("search").value.trim().toLowerCase();
    if (q) {
      const hay = entryHaystack(e);
      const terms = q.split(/\s+/);
      if (!terms.every(t => hay.includes(t))) return false;
    }
    const c = $("filter-corpus").value;
    if (c && e.corpus !== c) return false;
    const ip = $("filter-ip").value;
    if (ip && e.ip_status !== ip) return false;
    const quality = $("filter-quality").value;
    if (quality === "commons" && e.draft) return false;
    if (quality === "draft" && !e.draft) return false;
    const year = entryYear(e);
    const ymin = parseInt($("filter-year-min").value, 10);
    const ymax = parseInt($("filter-year-max").value, 10);
    if (!isNaN(ymin) && (year === null || year < ymin)) return false;
    if (!isNaN(ymax) && (year === null || year > ymax)) return false;
    const tag = $("filter-tag").value.trim().toLowerCase();
    if (tag) {
      const tags = (e.disclosed_subsystems || []).map(t => t.toLowerCase());
      if (!tags.some(t => t.includes(tag))) return false;
    }
    return true;
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function tagLink(tag) {
    return `<a class="tag" href="${baseurl}/cross_cuts/${tag}.html">${escapeHtml(tag)}</a>`;
  }

  function renderEntry(e) {
    const year = entryYear(e) || "?";
    const draftClass = e.draft ? "draft" : "commons";
    const draftText = e.draft ? "draft" : "commons-grade";
    const tags = (e.disclosed_subsystems || []).map(tagLink).join(" ");
    const tagsBlock = tags
      ? `<div class="tags" style="margin-top:0.4rem;">${tags}</div>`
      : "";
    const dl = [];
    function row(label, val) {
      if (val == null || val === "" || (Array.isArray(val) && val.length === 0)) return;
      const s = Array.isArray(val) ? val.join(", ") : String(val);
      dl.push(`<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(s)}</dd>`);
    }
    row("creator", e.creator);
    row("country", e.creator_country);
    row("device class", e.device_class);
    row("substrate", e.substrate_material);
    row("fabrication", e.fabrication_method);
    row("channel geometry", e.channel_geometry);
    row("flow regime", e.flow_regime);
    row("chip footprint mm", e.chip_footprint_mm);
    row("sample volume", e.sample_volume);
    row("throughput", e.throughput);
    row("power source", e.power_source);
    row("application", e.end_application);
    row("control", e.control_architecture);
    row("sensing", e.sensing);
    row("disclosure", e.disclosure_citation);
    row("ip status", e.ip_status);
    row("ip citations", e.ip_citations);

    const notes = e.prior_art_notes
      ? `<p style="margin:0.3rem 0;"><strong>prior art notes</strong> — ${escapeHtml(e.prior_art_notes)}</p>`
      : "";
    const sources = (e.sources && e.sources.length)
      ? `<p style="margin:0.3rem 0;"><strong>sources</strong> — ${e.sources.map(s => escapeHtml(s)).join("; ")}</p>`
      : "";

    return `<details class="entry">
      <summary>
        <div class="entry-head">
          <span class="entry-name">${escapeHtml(e.canonical_name)}</span>
          <span class="entry-year">${year}</span>
        </div>
        <div class="entry-meta">
          <span class="badge ${draftClass}">${draftText}</span>
          <span class="badge">${escapeHtml(e.corpus)}</span>
          <span class="badge">${escapeHtml(e.ip_status || "")}</span>
          <code>${escapeHtml(e.id)}</code>
        </div>
        ${tagsBlock}
      </summary>
      <div class="entry-body">
        <dl>${dl.join("")}</dl>
        ${notes}
        ${sources}
      </div>
    </details>`;
  }

  function render() {
    const sortKey = e => entryHaystack(e).startsWith($("search").value.trim().toLowerCase())
      ? 0 : 1;
    const filtered = entries
      .filter(matches)
      .sort((a, b) => {
        const yb = entryYear(b) || 0, ya = entryYear(a) || 0;
        return ya - yb || (a.canonical_name || "").localeCompare(b.canonical_name || "");
      });
    status.textContent = `${filtered.length} of ${entries.length} entries`;
    results.innerHTML = filtered.slice(0, 200).map(renderEntry).join("");
    if (filtered.length > 200) {
      results.innerHTML += `<p style="margin:1rem 0;opacity:0.7;text-align:center;">Showing first 200. Refine filters to see the rest.</p>`;
    }
  }

  render();
})();
</script>
