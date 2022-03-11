# 2022-02 Analytics Content

In 2022-02, we published 0 reports, 4 automations and 1 example using [crosscompute 0.9.1.4](https://pypi.org/project/crosscompute).

{ content-counts }

## Reports

We did not publish any reports in 2022-02.

## Automations

{ draft-investment-strategy }

- [Draft Investment Strategy](https://crosscompute.net/a/draft-investment-strategy) guesses investor sentiment for individual ticker symbols using put and call data. We use the tool to plan stock buy and sell targets.

{ title-videos }

- [Title Videos](https://crosscompute.net/a/title-videos) prepends a static image to a video for a specified number of seconds.

{ see-next-goals }

- [See Next Goals](https://crosscompute.net/a/see-next-goals) renders a report that ranks upcoming tasks across multiple documents. The public version shows upcoming tasks related to our open source packages as parsed from <https://github.com/crosscompute/missions>.

{ run-onsset }

- [Run OnSSET](https://crosscompute.net/a/run-onsset) is a thin wrapper around the [OnSSET electrification planning model](https://github.com/OnSSET/onsset) developed by the KTH Division of Energy Systems.

## Examples

{ randomize-histograms-batch-reference-folder }

- [Randomize Histograms](https://crosscompute.net/a/randomize-histograms) now includes an example of how to use a reference folder to set default values for missing values in a batch configuration ([see code](https://github.com/crosscompute/crosscompute-examples/blob/5173cb74d3e9c970dccc612dba1677ad074e9e49/reports/randomize-histograms/automate.yml#L73)). If you are using [jupyterlab-crosscompute](https://pypi.org/project/jupyterlab-crosscompute), we recommend installing the [jupyterlab-spreadsheet-editor](https://github.com/jupyterlab-contrib/jupyterlab-spreadsheet-editor) to edit your batch configuration tables.

{ compute-logarithms }

{ compute-logarithms-configuration }

- [Compute Logarithms](https://crosscompute.net/a/compute-logarithms) demonstrates how to use the table view for variables and how to add table styling using CSS.

## Announcements

- [crosscompute 0.9.1.4](https://pypi.org/project/crosscompute) of our open source development server replaces full page refresh with incremental variable refresh, resulting in a smoother user experience when running automations. Reference folders can be used to fill missing variables for batch configurations. The framework has tighter integration with jupyterlab-crosscompute through better error messages. Running `crosscompute --configure` will instantiate a configuration file with all available configuration options. Finally, we added two views: link, table.
- [crosscompute-views-map 0.1.1.2](https://pypi.org/project/crosscompute-views-map) supports incremental variable refresh.
- [crosscompute-printers-pdf 0.2.0](https://pypi.org/project/crosscompute-printers-pdf) can print pdfs from automations via `crosscompute --print pdf`.
- [jupyterlab-crosscompute 0.2.1](https://pypi.org/project/jupyterlab-crosscompute) adds support for launching our development server directly within JupyterLab.
- [Documentation for the framework](https://docs.crosscompute.com) is online. Please see [configuration.yaml](https://github.com/crosscompute/crosscompute/blob/develop/crosscompute/templates/configuration.yml) for available configuration options.

## Links

Reports

- [Locating Hospitals in Mayfield, Kentucky, USA](https://crosscompute.net/a/locating-hospitals-in-mayfield-kentucky-usa)

Automations

- [Draft Investment Strategy](https://crosscompute.net/a/draft-investment-strategy)
- [Title Videos](https://crosscompute.net/a/title-videos)
- [See Next Goals](https://crosscompute.net/a/see-next-goals)
- [Run OnSSET](https://crosscompute.net/a/run-onsset)
- [Find Places](https://crosscompute.net/a/find-places)
- [Send Emails](https://crosscompute.net/a/send-emails)

Examples

- [Randomize Histograms](https://crosscompute.net/a/randomize-histograms)
- [Compute Logarithms](https://crosscompute.net/a/compute-logarithms)
- [Paint Letters](https://crosscompute.net/a/paint-letters)
- [Map Schools](https://crosscompute.net/a/map-schools)
- [Show Maps](https://crosscompute.net/a/show-maps)
- [Add Numbers](https://crosscompute.net/a/add-numbers)
- [Ask Question](https://crosscompute.net/a/ask-question)
- [Gather Locations](https://crosscompute.net/a/gather-locations)
- [Manage Locations](https://crosscompute.net/a/manage-locations)

Posts

- [2022-01 Analytics Content](https://crosscompute.net/a/2022-01-analytics-content)
