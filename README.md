# FireCry

Detects the sizes of possible wildfires and the rate at which those fires are growing using Computer Vision/OpenCV. Gives a pre-emptive warning (phone alerts) to nearby individuals using Twilio. Has a MongoDB Stitch database of both surveillance-type videos (as in campgrounds, drones, etc.) and neightborhood cameras that can be continually added to, depending on which neighbors/individuals sign the agreement form using DocuSign.

FireCry uses different computer vision algorithms to classify fires from cameras/videos, in particular, those mounted on households for surveillance purposes. It calculates the relative size and rate-of-growth of the fire in order to alert nearby residents if said wildfire may potentially pose a threat. It hosts a database with multiple video sources in order for warnings to be far-reaching and effective.

# What is does

This software detects the sizes of possible wildfires and the rate at which those fires are growing using Computer Vision/OpenCV. The web-application gives a pre-emptive warning (phone alerts) to nearby individuals using Twilio. It has a MongoDB Stitch database of both surveillance-type videos (as in campgrounds, drones, etc.) and neighborhood cameras that can be continually added to, depending on which neighbors/individuals sign the agreement form using DocuSign.

# Difficulties

Among the difficulties I faced, I had the most trouble with understanding the applications of multiple relevant DocuSign solutions for use within our project as per our individual specifications. For example, I wasn't sure how I could use something like the text tab to enhance my features within the client's agreement. One other thing I was not not fond of was that DocuSign logged us out of the sandbox every few minutes, which was sometimes a pain. Moreover, the development environment sometimes seemed a bit cluttered at a glance, which discouraged the use of their API. There was a bug in Google Chrome where Authorize.Net (DocuSign's affiliate) could not process payments due to browser-specific misbehavior. This was brought to the attention of DocuSign staff. One more thing that was also unfortunate was that DocuSign's GitHub examples included certain required fields for initializing, however, the description of these fields would be differ between code examples and documentation. For example, "ACCOUNT_ID" might be a synonym for "USERNAME" (not exactly, but same idea).

# Accomplishments

I am quite satisfied with how I experimented with the power of enterprise solutions in making a difference while hacking for resilience. Wildfires, among the most devastating of natural disasters in the US, have had a huge impact on residents of states such as California. I have leveraged existing residential video footage systems for high-risk wildfire neighborhoods.

Tools:
- Twilio
- Flask
- DocuSign
- OpenCV
- ML w/ Python, Computer vision
- 2 Factor Auth
- Mongo DB / Stitch
- Bootstrap
- HTML5 / CSS3 / JS
