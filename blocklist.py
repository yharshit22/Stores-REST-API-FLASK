"""
blocklist.py

This file just contains the BLOCKLIST set used to store revoked JWT tokens. It will be imported by 
app and the logu=out resource so that tokens can be added to the blocklist when the user logs out.
"""

BLOCKLIST = set()