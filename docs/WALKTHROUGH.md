# Finsight v1 — Three-Minute Walkthrough

This is the narration and shot list for the dashboard walkthrough. Record the live dashboard or screen-capture the static demo at 1440×900. Keep the pacing conversational and leave the caveats on screen when they are mentioned.

| Time | Screen | Narration |
|---|---|---|
| 00:00–00:20 | Open on the Finsight readout and the headline. | “This is Finsight v1: an evidence-first read of UPI app growth. The question is not just whether UPI is getting bigger. It is whether that growth is broadening across apps or staying concentrated in a small number of defaults.” |
| 00:20–00:45 | Pan across the four headline metrics. | “The dataset contains 1,482 verified app-month rows across 107 reported apps. In the verified record, monthly volume rises from 11.16 billion transactions in November 2023 to 19.97 billion in October 2025—an increase of about 78.9 percent.” |
| 00:45–01:20 | Toggle the Evidence chart from Volume to Top-two share. | “The volume line is the easy part of the story. The concentration line is the important part. PhonePe and Google Pay together account for 83.01 percent of October 2025 transaction volume. That share has moved, but it remains high enough that a growing market should not be mistaken for an open market.” |
| 01:20–01:45 | Change the app lens month and show the ranking bars. | “The app lens makes the distribution concrete. The month selector is not a cosmetic filter: it lets you inspect the leading apps and their volume shares in each verified month. The long tail is kept in NPCI’s own reporting bucket rather than reverse-engineered here.” |
| 01:45–02:15 | Scroll to Projection and pause on chart and table. | “The projection uses one deliberately simple model: linear regression on total monthly transaction volume against a calendar-month index. It projects 20.22 billion for November 2025, 20.59 billion for December, and 20.96 billion for January 2026. The dashed range is an approximate residual band, not a confidence theater.” |
| 02:15–02:40 | Hold on the model cards. | “The last four real months were held out as a temporal test. Test MAPE is 1.69 percent versus 2.15 percent on train. That does not make the model reliable in every future regime. There is no seasonality term, the sample is only 19 verified months, and the future can miss this band.” |
| 02:40–02:55 | Hold on “Why 19 of 24?” | “Why 19 instead of 24? Five months were byte-identical to their preceding month in the app-wise export. They were excluded, not patched or interpolated. This is a named limitation, because honest missingness is better than precise-looking fiction.” |
| 02:55–03:00 | End on provenance and repository link. | “The source trail points back to NPCI’s public UPI Ecosystem Statistics. The repository contains the raw archive, cleaning notes, SQL, model, memo, validation script, and release decisions. Finsight’s answer is simple: UPI is growing, but distribution is still the moat.” |

## Recording notes

Use the dashboard’s visible source dockets as lower-third anchors. Do not add stock footage, AI-generated narration, or claims that are not present in the repository. If the video is not embedded in the public demo, keep this script and a recorded MP4 in the release assets so the walkthrough remains reproducible.
