##Question 2:
**Investigate Moat Ad Search (http://moat.com) and tell us about all of its
functionality from a user's perspective. Also please explain how you would test those features manually: the sorts of bugs you would look for and some
of the test cases you would go through. We are not asking for bug reports,
just thoughts about how you would validate the behavior of the site and try
to break it. You can either do a deep dive describing how you would test a
particular feature or tell us in broad terms how you would test the site’s
many features.**



On the ad search page the first thing you notice is the heading "Ad Search" and the filler text that says "Search by brand". The magnifying glass submit button pops out because of its location and color. The fact that the background image is black & white helps focus user attention on the most important feature of the page and minimizes eye strain. It's convenient that there are suggested companies to research. I think it makes the input field less intimidating and lets the user check out functionality even if they don't know what company they want to research.

The next thing to grab the user's attention is the bar with the recently seen ads. I like that they're small so that you notice them but they don't draw your attention away from the main search input. Seeing the heading "Recently seen ads" I would think that these were ads recently seen by me but I don't actually recognize any of the ads. It's obvious what I can click on by the hand appearing at mouseover. As for the third main section of the page, it's nice that the video pops up without navigating away from the page and that it starts out on mute. And the footer bar is helpful for finding my way around the site easily.

To manually test the page. I would start by making my way down the page and checking that all of the links work. As I was checking the links I would make sure that each page had consistent styling. I would note anything that looked odd. I would search random companies and check that the ad results were all for the correct company. I would randomly check that the mouseover events are firing correctly and that each link inside the popup worked. I would check that every feature had the elements it was supposed to have. I'd be looking to see if the links went where expected. If event handlers fired as expected. I'd try to search brands with fewer ads to check that the counts were correct. I'd click on things to see what happened, noting any error messages. I'd randomly inspect element. I'd check if elements that aren't supposed to be clickable are. I'd look for error messages.
