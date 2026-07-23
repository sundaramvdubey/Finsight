create table if not exists upi_monthly_app (
    id            bigint generated always as identity primary key,
    month_start   date not null,
    app_name      text not null,
    volume_mn     numeric not null,
    value_cr      numeric not null,
    source_file   text,
    loaded_at      timestamptz default now(),
    unique (month_start, app_name)
);

create table if not exists app_reference (
    app_name      text primary key,
    display_name  text,
    is_long_tail  boolean default false,
    notes         text
);