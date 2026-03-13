#!/bin/bash
# Deploy nikitacometa.dev to Hostinger VPS
# Usage: npm run deploy

set -euo pipefail

REMOTE_HOST="hostinger"
REMOTE_PATH="~/nikitacometa.dev"

echo "Building..."
npm run build

echo "Deploying to $REMOTE_HOST:$REMOTE_PATH..."
rsync -avz --delete dist/ "$REMOTE_HOST:$REMOTE_PATH/"

echo "Done. Site live at https://nikitacometa.dev"
