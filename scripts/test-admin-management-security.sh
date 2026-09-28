#!/usr/bin/env bash
set -euo pipefail
for url in /api/admin/published-workers; do
  status=$(curl -sS -o /tmp/labrkp-admin-management.json -w '%{http_code}' "http://localhost:3000${url}")
  test "$status" = "401"
done
public_status=$(curl -sS -o /tmp/labrkp-public-feed.json -w '%{http_code}' http://localhost:3000/api/workers/public)
test "$public_status" = "200"
printf 'admin_management_status=401 public_feed_status=%s\n' "$public_status"
