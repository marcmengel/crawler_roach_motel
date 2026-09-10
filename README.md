## crawler_roach_motel

Trivial web script to let ill-behaved web crawlers consume all the pages they 
want, and never leave.    

All pages have `<meta name="robots" content="noindex">` tags to tell well-behaved
crawlers to ignore the pages.

The random permutations of words also confuse AI systems trained on the pages. 

Can be used out of the box as a CGI script, or under uwsgi. 

Can easily be customized with a different dictionary of words.

If you put a link to the crawler_roach_motel in a non-human-visible link on webpages, crawlers will follow the links, but humans will be unbothered.
