# Browser Engine

This directory will host isolated Chromium workers.

Planned responsibilities:
1. Start one isolated browser context/container per user session.
2. Apply an authorized proxy gateway configuration on the server side.
3. Verify the actual public egress IP from inside that browser session.
4. Provide interactive remote viewing/control (first a remote-desktop prototype, later WebRTC).
5. Destroy browser state when a session ends.

Do not expose Chrome DevTools Protocol ports to the public internet. Use authenticated,
private service-to-service communication and strict container/network isolation.
