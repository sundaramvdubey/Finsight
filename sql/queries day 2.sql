-- Finsight Day 2 SQL — run each block separately in the Supabase SQL Editor,
-- sanity-check the output, then move to the next.

-- =========================================================
-- 1. Market share over time (window function)
-- Volume-share is primary per DECISIONS.md; value-share included as cross-check.
-- =========================================================
select
    month_start,
    app_name,
    volume_mn,
    value_cr,
    round(100.0 * volume_mn / sum(volume_mn) over (partition by month_start), 2) as volume_share_pct,
    round(100.0 * value_cr  / sum(value_cr)  over (partition by month_start), 2) as value_share_pct
from upi_monthly_app
order by month_start, volume_share_pct desc;


-- =========================================================
-- 2. Month-on-month growth (window function)
-- Null mom_change on an app's first appearance is expected, not a bug.
-- =========================================================
select
    month_start,
    app_name,
    volume_mn,
    lag(volume_mn) over (partition by app_name order by month_start) as prev_month_volume,
    round(
        volume_mn - lag(volume_mn) over (partition by app_name order by month_start), 2
    ) as mom_change_mn,
    round(
        100.0 * (volume_mn - lag(volume_mn) over (partition by app_name order by month_start))
        / nullif(lag(volume_mn) over (partition by app_name order by month_start), 0), 2
    ) as mom_growth_pct
from upi_monthly_app
order by app_name, month_start;


-- =========================================================
-- 3. Rankings per month (window function)
-- =========================================================
select
    month_start,
    app_name,
    volume_mn,
    rank() over (partition by month_start order by volume_mn desc) as rank_in_month
from upi_monthly_app
order by month_start, rank_in_month;


-- =========================================================
-- 4. Concentration over time (CTE + HHI)
-- HHI = sum of squared market shares (as fractions, not %). Ranges 0-1 here;
-- multiply by 10,000 for the conventional 0-10,000 HHI scale.
-- Includes Top-2 (PhonePe+GPay) share as a second, more intuitive lens.
-- =========================================================
with shares as (
    select
        month_start,
        app_name,
        volume_mn / sum(volume_mn) over (partition by month_start) as share
    from upi_monthly_app
),
hhi as (
    select month_start, round(sum(power(share, 2)) * 10000, 0) as hhi_score
    from shares
    group by month_start
),
top2 as (
    select month_start, round(100.0 * sum(share), 2) as top2_share_pct
    from shares
    where app_name in ('PhonePe', 'Google Pay')
    group by month_start
)
select h.month_start, h.hhi_score, t.top2_share_pct
from hhi h
join top2 t on t.month_start = h.month_start
order by h.month_start;


-- =========================================================
-- 5. CRED-specific trend (so-what for the memo)
-- =========================================================
select
    month_start,
    volume_mn,
    round(100.0 * volume_mn / sum(volume_mn) over (partition by month_start), 3) as volume_share_pct,
    rank() over (partition by month_start order by volume_mn desc) as rank_in_month
from upi_monthly_app
where app_name = 'Cred'
order by month_start;
