# OrgaTalk LAN Party Database Format Specification


## File Format

The data is represented in the form of flat files, formatted in
[TOML](https://toml.io/) syntax. This should make the data sufficiently easy to
read and write by both humans and computers.

Use line feeds (LF) as end-of-line characters. Do not put blank lines (just a
single line feed) at the end of each file.


## Structure

For now, the only things modeled are LAN parties, and LAN party series.

Not every party belongs to a series, though! Some are just one-time events.


### Party Series

Each party series should be defined in its own file, which should be named
`<series slug>.toml`, in path [`./data/series`](./data/series).

A series *must* specify:

* A `slug`, which is an identifier that can nicely be used in URLs and the
  filesystem. It may only contain lower-case latin characters, numbers, and
  dashes.
* A `title`, which does not have the slug's limitations.
* `country_codes`, which is a non-empty list of two-letter [ISO 3166-1
  alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)
  country codes.

A series *may* have:

* `alternative_titles`, which is a non-empty list of alternative titles of the
  party series.
* A `links` section; see below.

A links section *must* have:

* A `website`, which:

  * *must* specify `url`, which is a common URL like
    `https://www.awesomelan.example/`.
  * *can* specify `offline`, with a value of either `false` (the default) or
    `true`.

Minimal series example:

```toml
slug = "awesome-lan"
title = "Awesome LAN"
```

Full series example:

```toml
slug = "awesome-lan"
title = "Awesome LAN"
alternative_titles = ["That Awesome LAN Party"]
country_codes = ["ca"]

[links.website]
url = "https://www.awesomelan.example/"
```


### Parties

Parties eligible for inclusion at this point have to be **public** and **in the
past**.

Each party should be defined in its own file, which should be named `<party
slug>.toml`.

If the party is part of a series, it should be in path `./data/parties/<series
slug>`; if it is not, it should be in [`./data/parties`](./data/parties).

A party *must* have:

* A `slug`, which is an identifier that can nicely be used in URLs and the
  filesystem. It may only contain lower-case latin characters, numbers, and
  dashes.
* A `title`, which does not have the slug's limitations.
* A start date, `start_on`. Format: `YYYY-MM-DD`, without surrounding double
  quotes.
* An end date, `end_on`. Same format as `start_on`.

A party *may* have:

* A `series_slug`, *if* the party belongs to a series (see above).
* An `organizer_entity`, if that is somewhat relevant, maybe because it
  significantly changed at some point. If its just "a bunch of people" for the
  duration of the party, you can just leave it out. Can be a single string or
  an array of multiple strings.
* A number of `seats`. This should be the number of seats the party actually
  offered, not the number of attendees.
* A number of `attendees`. This should be the number of attendees the party
  had, or the number of tickets sold if only that information is available.
* `online = true`, *if* the party was online-only (e.g. during a pandemic). In
  this case, the `location` section must not be provided.
* A `location` section; see below.
* A `links` section; see below.

A location section *must* have:

* A country in the form of a two-letter `country_code`, which must be an [ISO
  3166-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)
  value.
* A `city`.

A location section *may* have:

* The `name` of the location.
* A `postal_code`, if the country has such a thing.
* A `street` name and, if applicable, house number.
* Geographic coordinates in the form of both `latitude` and `longitude` values.

A links section *must* have:

* A `website`, which:

  * *must* specify `url`, which is a common URL like
    `https://www.awesomelan.example/` or
    `https://www.awesomelan.example/parties/23`.
  * *can* specify `offline`, with a value of either `false` (the default) or
    `true`.


Minimal party example:

```toml
slug = "awesomemest-lan"
title = "Awesomest LAN"
start_on = 2001-07-27
end_on = 2001-07-29

[location]
country_code = "de"
city = "Büttenwarder"
```

Full party example:

```toml
slug = "awesome-lan-4"
title = "Awesome LAN #4"
series_slug = "awesome-lan"
organizer_entity = "Awesome LAN e.V."
start_on = 2000-07-28
end_on = 2000-07-30
seats = 32
attendees = 23

[location]
name = "Gasthof zum Wattwurm"
country_code = "de"
city = "Büttenwarder"
postal_code = "22999"
street = "Kirchweg 7"
latitude = 54.03847
longitude = 8.25632

[links.website]
url = "https://www.awesomelan.example/"
```


## Changelog


### 0.11 (2025-12-13)

* Moved series into a separate file each.


### 0.10 (2025-12-13)

* Renamed series property `name` to `title`.
* Renamed series property `alternative_names` to `alternative_titles`.
* Added optional links section for series.


### 0.9 (2025-04-04)

* Renamed property `zip_code` to generic `postal_code` in section `location`.


### 0.8 (2025-03-10)

* Require property `country_codes` in section `series`.


### 0.7 (2024-07-01)

* Added optional property `country_codes` to section `series`.


### 0.6 (2024-06-30)

* Required websites to be specified with the `url` property in section
  `website` instead of using `website` as a property with string value.


### 0.5 (2024-05-16)

* Added optional property `attendees` to section `party`.


### 0.4 (2024-02-14)

* Allowed `organizer_entity` to alternatively be an array with multiple values.


### 0.3 (2024-02-13)

* Made property `name` in section `location` optional.


### 0.2 (2024-02-09)

* Added optional flag `online` to section `party`.
* Prohibited section `location` for online events.
* Added optional flag `offline` to section `website`.


### 0.1 (2024-01-30)

* Created initial format.
