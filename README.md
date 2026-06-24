# askMe - Personal Portfolio MCP Server

> Make your work queryable by AI agents

An MCP (Model Context Protocol) server that lets AI agents — Claude Desktop, Claude.ai, Cursor, Amp — answer questions about your work, projects, and experience. Built with Python, FastAPI, and deployed to the web for zero-friction access.

## What It Does

Turn your portfolio into a live API for AI agents. Instead of making people read your resume or browse GitHub, let them ask questions in natural language and get grounded answers from your actual work.

## Use Cases

**For Job Seekers:**
A recruiter adds your URL to Claude.ai and asks *"does this candidate have Kubernetes experience?"* Claude calls your tools, finds relevant projects, and gives a grounded answer with links. No GitHub browsing required.

**For Content Creators:**
A podcast host preparing an interview asks *"what are their most controversial takes?"* Your server searches your blog posts and returns specific articles with context.

**For Open Source Maintainers:**
A contributor asks *"how does the authentication flow work?"* Your server returns architecture docs, code snippets, and relevant implementation details from your project.

**For Consultants:**
A potential client asks *"have you worked with companies in healthcare?"* Your server pulls from your experience database and case studies.

## Why Build This

- **Direct marketing.** Make your work discoverable in the way people actually want to consume it, through conversation.
- **Web-accessible from day one.** Deployed with HTTP/SSE transport — anyone connects via a URL, no installs, no repo cloning.
- **Template for others.** Fork, customize with your content, deploy your own version.
