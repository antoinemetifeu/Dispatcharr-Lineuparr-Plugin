"""
Built-in blocked stream table for Lineuparr.
Maps lineup channel names to stream name patterns that should never match
that channel. Patterns are matched by normalized name (provider prefix
stripped, quality preserved) so "TF1 4K HDR" blocks "FR - TF1 4K HDR",
"FR: TF1 4K HDR", etc. regardless of provider prefix.
User-configured custom_blocked_streams are merged on top of these.
"""

CHANNEL_BLOCKED_STREAMS = {
    # --- FR: Event-only 4K streams ---
    # These streams broadcast trailers or promos on loop and are not
    # full-schedule channels. They should not be matched to any channel.
    "TF1 UHD": ["TF1 4K HDR"],
    "M6 UHD": ["M6 UHD 4K", "M6 4K HDR"],
}
