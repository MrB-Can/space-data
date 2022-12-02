# PAUL's PIPES | Space Data
This is a tool to generate space data from multiple sources. This is part of paulspipes, a data generation system for demo and testing data for different data and database types. Space Data is only one of the many components to Paul's Pipes. All of the other data systems are private, but I am happy to make redacted soutions available publically. 
## Sources and credits
Thanks to the main sources that made this possible:
NORAD
NASA
n2yo
## Modules
There are seeral modules for creating data for testing. 
### NORAD Objects
Up to date information on all NORAD tracked objets since the first object sent to space. This system relies on NORAD identifiers which I've made publically available here. 
#### Purpose
This is intended to be run by CLI or serverless function and insert objects into a single table in a database for us in analytics, demonstrations, or testing. 
#### Functions
