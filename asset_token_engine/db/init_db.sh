#!/bin/bash
# Usage: ./init_db.sh

psql -U postgres -d one_stop_finance -f db/schema.sql
