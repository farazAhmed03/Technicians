#!/usr/bin/env bash
set -euo pipefail
reply_status=$(curl -sS -o /tmp/labrkp-reply-denied.json -w '%{http_code}' -X POST http://localhost:3000/api/workers/1/reviews/fake-review/reply -H 'Content-Type: application/json' -d '{"reply":"Thanks"}')
admin_status=$(curl -sS -o /tmp/labrkp-review-admin-denied.json -w '%{http_code}' http://localhost:3000/api/admin/reviews)
admin_delete_status=$(curl -sS -o /tmp/labrkp-review-delete-denied.json -w '%{http_code}' -X DELETE http://localhost:3000/api/admin/reviews/fake-review)
test "$reply_status" = "401"
test "$admin_status" = "401"
test "$admin_delete_status" = "401"
printf 'worker_reply=%s admin_reviews=%s admin_delete=%s\n' "$reply_status" "$admin_status" "$admin_delete_status"
