---
title: piezo-printhead
parent: Cross-cuts
layout: default
---

# Cross-cut: `piezo-printhead`

**6 corpus entries disclose this subsystem.**

Earliest disclosure: 2014

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Mutoh ValueJet 1638UH / 1638UR UV-LED Inkjet Printer (2014)

- **id**: `mutoh-valuejet-1638uh-uv-led-printer`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Mutoh Industries Ltd.
- **disclosure**: Mutoh Industries Ltd. ValueJet 1638UH product launch 2014; VJ-1638UH MkII datasheet 2018
- **ip status**: patented
- **prior art notes**: Discloses a wide-format UV inkjet printer with Mutoh's piezo printhead and Intelligent Interweaving banding-reduction algorithm. Anticipates: wide-format UV inkjet printers using shuttle-mounted piezo printhead with CMYK+W+V channel allocation and pass-pattern algorithms for banding reduction. Mid-tier wide-format competitor to Mimaki and Roland.

## Brother GTX/GTX600 Direct-to-Garment Printer (2017)

- **id**: `brother-gtx-direct-to-garment-printer`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Brother Industries, Ltd.
- **disclosure**: Brother GTX launch 2017; GTX600 launch 2022; Brother GTX product brochure 2017; Brother USA garment printer datasheet
- **ip status**: patented
- **prior art notes**: Brother's DTG entry whose architectural innovation is the 6-channel printhead allocation (CMYK + 2 white) doubling white throughput on dark garments. Anticipates: DTG printheads with multiple white channels in parallel to overcome the white-throughput bottleneck of single-white-channel DTG architectures. GTX600 extends to direct-to-film (DTF) workflow where white+CMYK is printed onto a PET film, dusted with hot-melt powder, then heat-pressed onto garments - an architectural alternative to direct-to-garment that defends against many DTG patents by routing through an intermediate.

## Markforged / Digital Metal DM P2500 Binder Jet Printer (2017)

- **id**: `markforged-digital-metal-binder-jet`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Markforged Inc. (Digital Metal product line via 2022 acquisition; originally Hoganas Digital Metal AB, Sweden)
- **disclosure**: Digital Metal AB (Hoganas Group subsidiary, acquired by Markforged 2022) DM P2500 launch 2017; Markforged Digital Metal datasheet 2023
- **ip status**: patented
- **prior art notes**: Discloses a metal binder-jetting architecture optimized for fine-feature parts via small-particle metal powder. Anticipates: metal binder-jet printers using sub-10-micron metal powder with piezo printhead binder deposition followed by debind/sinter, particularly the fine-particle handling and powder spreading challenges that conventional 25-50 micron metal binder-jet systems do not address. Useful prior art for any high-resolution metal binder-jet patent claim.

## Mutoh XpertJet XPJ-460PRT Direct-to-Garment Printer (2017)

- **id**: `mutoh-xpj-460prt-direct-to-garment`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Mutoh Industries Ltd.
- **disclosure**: Mutoh XpertJet XPJ-460PRT direct-to-garment printer launch 2017; Mutoh DTG datasheet
- **ip status**: patented
- **prior art notes**: Mutoh's DTG entry following the Brother/Ricoh pattern: piezo printhead with dual-white channels and recirculation, on a platen shuttle transport. Architectural primitives shared with Brother GTX and Ricoh Ri 1000 series. Anticipates: compact-tabletop DTG printers with dual-white-channel allocation and white-ink recirculation.

## Ricoh Ri 1000/2000/6000 Direct-to-Garment Printer Series (2018)

- **id**: `ricoh-ri-garment-printer-series`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Ricoh Company, Ltd. (Garment Printers Division, formerly AnaJet Inc.)
- **disclosure**: Ricoh acquisition of AnaJet 2018 forming Ricoh Garment Printers Division; Ricoh Ri 1000 launch 2019; Ricoh Ri 2000 launch 2020
- **ip status**: patented
- **prior art notes**: Discloses a DTG printer architecture whose key fluidic primitive is white-ink recirculation: titanium-dioxide pigment in the white channel will sediment in static plumbing within hours, so the printhead and supply lines integrate a recirculating loop that continuously moves white ink past the nozzles even when not printing. Anticipates: DTG printers using piezo printheads with active ink-recirculation specifically for white-ink stability, plus a platen-shuttle transport for garment positioning. The (recirculating white channel + piezo printhead + platen shuttle + pretreatment-cured cotton substrate) architecture defines modern DTG.

## Roland VersaUV LEJ-2/LEF-2/LEC2 UV Inkjet Series (2019)

- **id**: `roland-versauv-lej2-flatbed-uv`
- **corpus**: private
- **device class**: inkjet-printhead
- **creator**: Roland DG Corporation
- **disclosure**: Roland DG VersaUV LEC2 launch 2019; LEF2 launch 2020; Roland VersaUV product datasheets
- **ip status**: patented
- **prior art notes**: Discloses Roland's UV-inkjet platform whose architectural primitives include: (1) the multi-pass-build-up workflow for 3D tactile textures (each pass deposits and cures a sub-100-micron layer; many passes build mm-scale texture); (2) selective Gloss/Matte finishes via a clear-ink channel applied selectively per pixel; (3) Primer channel laid first to bond UV ink to non-receptive substrates (acrylic, glass, metal). Anticipates: small-format UV printers using primer + CMYK + white + clear-coat channel allocation with multi-pass-build-up texture workflows and selective gloss/matte finishing.
