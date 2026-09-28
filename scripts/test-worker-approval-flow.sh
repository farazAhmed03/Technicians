#!/usr/bin/env bash
set -euo pipefail
base='http://localhost:3000'
payload='{"name":"Demo Worker","phone":"03001234567","email":"demo.worker@example.com","gender":"Male","city":"Peshawar","skill":"Other","customSkill":"Mobile repair","experience":"4 years","bio":"Demo application for admin review","consent":true}'
created=$(curl -fsS -X POST "$base/api/workers/apply" -H 'content-type: application/json' -d "$payload")
printf '%s\n' "$created"
id=$(printf '%s' "$created" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>process.stdout.write(JSON.parse(s).application.applicationId))')
queue=$(curl -fsS "$base/api/admin/worker-applications")
printf '%s\n' "$queue"
approved=$(curl -fsS -X PATCH "$base/api/admin/worker-applications/$id" -H 'content-type: application/json' -d '{"status":"Approved","reviewNote":"Demo verification passed"}')
printf '%s\n' "$approved"
