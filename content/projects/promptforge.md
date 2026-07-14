---
type: project
name: promptforge
tags: [ai, saas, openai, replicate, stripe, nextjs, prisma, redis]
github: https://github.com/UmukoroG/PromptForge
summary: Full-stack AI SaaS integrating OpenAI and Replicate for generation, with Stripe billing and 100k+ conversation scale
---

## What it is
PromptForge is a full-stack AI SaaS application built around OpenAI GPT-3.5
and Replicate APIs, offering conversation, code generation, and music
creation features to end users.

## What I built
- Integrated OpenAI GPT-3.5 and Replicate for three distinct generation
  modes (conversation, code, music), with comprehensive error handling and
  30-60 second response times.
- Built a tiered subscription system on Stripe — a free tier (5
  generations) and a Pro tier ($20/month unlimited) — including the in-app
  checkout flow, webhook handling, and real-time usage tracking backed by
  Prisma ORM.
- Implemented cursor-based pagination with infinite scroll for
  conversation history, cutting query time by 80% on large datasets.
- Added rate limiting (5 req/min) via Upstash Redis with retry logic and
  exponential backoff to prevent API abuse, scaling the system to 100k+
  conversations at 99.9% uptime.

## Stack
Next.js, TypeScript, Prisma ORM, Stripe, Upstash Redis, OpenAI API,
Replicate API.