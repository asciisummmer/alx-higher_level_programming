#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const firstSource = fs.readFileSync(process.argv[2], 'utf-8');
const secondSource = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], firstSource + secondSource);
