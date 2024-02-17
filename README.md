# Chatbot

A text-only chatbot based on AI systems written in Node.js

- [Description](#description)
- [Instructions](#instructions)
  - [Requirements](#requirements)
  - [Installing](#installing)
  - [Usage](#usage)
- [Contributing](#contributing)
- [Notes](#notes)

## Description

## Instructions

Put active credentials in a `.env` file:

```
OPENAI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your own API key.

Please, keep in mind that [OpenAI](https://openai.com/) checks for public API keys, so **it will be invalidated if you publish it** somewhere on the web.

### Requirements

- [Node.js](https://nodejs.org/)
- [Express](https://expressjs.com/)
- [TypeScript](https://www.typescriptlang.org/)
- [Rollup](https://rollupjs.org/)
- [OpenAI](https://openai.com/)

### Installing

```
npm install
npm run build
```

### Usage

```
npm run start
```

Express will start a server at `localhost` listening on port `9000`.

## Contributing

Please, use [SemVer](https://semver.org/) and [Conventional Commits](https://www.conventionalcommits.org/) in pull requests. [Hacktoberfest](https://hacktoberfest.com/) participants are welcome.

### Notes

It works with **Node.js v20.x** or higher.
