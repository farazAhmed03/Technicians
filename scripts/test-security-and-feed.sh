#!/usr/bin/env bash
set -euo pipefail
admin_status=$(curl -sS -o /tmp/labrkp-admin-denied.json -w '%{http_code}' http://localhost:3000/api/admin/worker-applications)
public_status=$(curl -sS -o /tmp/labrkp-public-feed.json -w '%{http_code}' http://localhost:3000/api/workers/public)
test "$admin_status" = "401"
test "$public_status" = "200"
printf 'admin_status=%s public_feed_status=%s\n' "$admin_status" "$public_status"
