[original project proposal](/Cartis+Outline+for+Final+Project+Proposal.pdf) | [peer review 1](/peerReview/Peer%20Review%201%20-%20Georg%20Clavin.pdf) | [peer review 2](/peerReview/Simion%20Cartis%20Peer%20Evaluation.pdf) | [Instructor Feedback](/peerReview/InstructorFeedback.png) | [revised project proposal](/CSCE567%20Project%20Proposal%20Revised.pdf)
## Changes Made to Proposal
- The second peer review argued that I should provide an explanation as to why I thought race and income may have an effect on who votes, so I added a brief explanation to the introduction section.

- Both the instructor and the second peer review suggested more visuals, with the second peer review specifically suggesting a scatter plot. Seeing this as a good idea, I took up the suggestion and added scatter plots. An additional visualization group for this is now added to the proposed visualizations section.

- Seeing as neither a layered histogram nor a normal histogram was used in the third visualization group, I removed them and replaced the description with what was actually used (a grouped and normal bar chart).

## Problems Encountered
The biggest problem I encountered was data reformatting/cleaning. All of my datasets were .xlsx files instead of .csv files, meaning they all had odd formatting that needed alteration before they could be used in any way. This was especially true for the "tableA2.xlsx" Excel sheet (the one on racial income) which had the years in the same columns as the races. I differentiated between the year and race information using regular expressions and placed them into separate columns.
However, even after reformatting the data (all of which was done in the reformatData folder), there was still often excess data that was unnecessary for my visuals, as I wanted to take the broadest amount of data possible initially and then filter it down further for a given visualization. Again, this was especially troublesome for the tableA2 excel sheet because it had significantly more race groupings than the others, and due to changes to data collection, some of these racial groups had disjoint years and/or repeated years. I dealt with this by running through a reformatted version of the original excel sheet and only keeping the racial groups that were shared with the hst_vote01 excel sheet and had the most modern data as well as the years with the highest sample size (for years that were repeated).

## Design Decisions
### Color Scheme
I chose black as my background color for all of my graphs because I wanted a higher contrast for the data points, which I think was especially helpful for the scatter plots, because the 4 points were easy to lose against a white background.
For the data points, I chose px.colors.qualitative.G10 because I felt it gave a good contrast between each race which was especially important for the first line chart, as often the lines overlapped.

### Interactive Elements
All interactive elements were created by the plotly.express Python extension. The main two interactive elements that I find the most important are the hover element and removing/adding elements to a visual. The hover element gives you exact numbers for a given data point, which is useful for actually understanding what values a specific data point has, and adding/removing elements allow you to focus on specific parts of a visual if you so choose.
Additionally, the ability to play through the different scatter plots is useful for seeing change over time while keeping the scatter plot simple and 2d.

### Graph Choices
I chose line charts for my first visualization as I wanted to show the change over time of both income and voting percentage for all 4 races. However, to prevent cluttering as well as to show the relation between race and voting percentage without the impact of income, there are two line charts.
The scatter plot visualizations are essentially attempting to show the same thing. However, there is more emphasis on the interaction between race, racial income, and voting percentage. Additionally, because the midterms consistently have a lower voter turnout, it can be hard to understand trends over time in the first scatter plot. Therefore, I created two more, one for the primaries and the other for the midterms to better show trends for both.
For the last grouping of visuals, I chose to represent voter percentage for family income ranges with a bar chart because I felt it best showed the distribution for each income range. The addition of the grouped bar chart showing income distribution per race and the normal bar chart showing voting percentage by race was included to show that, while there is a correlation between income range and voting percentage, that correlation is lost when you also look at racial patterns. A grouped bar chart for income distribution per race was chosen because I needed to show the percentage of multiple races for a given income range, and the bar chart for voting percentage per race was chosen because I believed it was a succinct and simple way to show voting trends for a single year (as opposed to over time like in the line charts).

### Visuals Not Used
- The line charts in the first grouping of visuals could have been put into a single chart that had two different y-axes (called a dual axis chart). However, I decided against that to prevent visual clutter and to more easily understand the relation between race and voting percentage.

- I considered making 3d scatter plots for my second grouping of visuals with time being the third dimension. However, I figured that keeping it 2 dimensional with a slider would achieve the same effect of showing a change over time (maybe even better than with a 3rd dimension) while keeping the layout simple and straight forward.

- The grouped bar chart in the last visualization group was originally a stacked bar chart. However, I realized that did not make much sense, as each subgroup of a bar was not part of the same whole, so it was changed to a grouped bar chart.

## Future Work
Seeing that there is a relationship between annual income range and voting percentage, additional visuals can be made to show how this relation changes over time. However, I currently do not have any data before 2024 regarding this, meaning I would have to first find data that shows voting percentage for income ranges over time. Once this data is found and cleaned, a line chart similar to the ones created for the first visual groupings can be made.
To further expand on the racial aspects, additional data from individuals who marked two or more racial groups could be acquired and the current visualizations that already exist can be expanded to include these entries as well.

## Sources Used:
[Reported Voting and Registration by Race](/data/hst_vote01.xlsx) | [Households by Total Income](/data/tableA2.xlsx) | [Reported voting and registration by Family Income](/data/vote07_2024.xlsx)