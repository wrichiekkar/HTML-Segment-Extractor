# Used to collect specific data from HTML of multiple webpages

The idea behind this project was to automate data collection for a major project. The way this script works is that it uses python requests to open up a page from a .txt file. It then opens up the source code and looks for the section specified. In this specific case, the data I needed was located in the title attribute, so it was designed to collect the link in the title. Once it found the link, it exported it to a .txt file with the original page link to the right of it.

EX: Collected README's from github repositories

Tried to use for Bell's accessibility project, but couldn't due to requests not being compatibile with javascript, refer to: https://github.com/wrichiekkar/Segment-Selector-With-Selenium
