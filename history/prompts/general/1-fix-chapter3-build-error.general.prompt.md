---
id: 1
title: "Fix Chapter3 Build Error"
stage: "general"
date: "2025-12-12"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "saira"
command: "Fix build error in chapter3.mdx"
labels: ["bug-fix", "build", "mdx", "template-variables"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "textbook-site/docs/module-4-vla/chapter3.mdx"
tests: []
---

## PROMPT_TEXT
When we are performing task T057, form tasks.md, i.e running "npm run build", an error is showing, stating there is an issue in the file chapter3.mdx of folder module-4-vla, from textbook-site/, this is the error that is showing in the terminal: [ERROR] Error: Unable to build website for locale en.
    at tryToBuildLocale (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\build.js:83:15)
    at async C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\build.js:35:9
    at async mapAsyncSequential (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\utils\lib\jsUtils.js:21:24)
    at async Command.build (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\build.js:34:5)
    at async Promise.all (index 0)
    at async runCLI (C:\Uselib\ssg\ssgExecutor.js:30:68
        at async executeSSG (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\ssg\ssgExecutor.js:144:20)
        at async buildLocale (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\buildLocale.js:84:31)
        at async runBuildLocaleTask (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\build.js:98:5)
        at async C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\build.js:79:13
        at async tryToBuildLocale (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\build.js:75:9)
        at async C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\commands\build\build.js:35:9
        at async mapAsyncSequential (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\utils\lib\jsUtils.js:21:24) {
      [errors]: [
        Error: Can't render static file for pathname "/humanoid-ai-textbook/docs/module-4-vla/chapter3"
            at generateStaticFile (C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\@docusaurus\core\lib\ssg\ssgRenderer.js:131:20)
            at async C:\Users\saira\OneDrive\Documents\Hackathon\humanoid_ai_textbook\humanoid_ai_book\textbook-site\node_modules\p-map\index.js:57:22 {          [cause]: ReferenceError: ROBOT_NAME is not defined
              at _createMdxContent (server.bundle.js:39343:9)
              at MDXContent (server.bundle.js:39660:8)
              at renderWithHooks (server.bundle.js:23263:18)
              at renderElement (server.bundle.js:23401:14)
              at retryNode (server.bundle.js:24119:16)
              at renderNodeDestructive (server.bundle.js:23913:7)
              at renderElement (server.bundle.js:23846:11)
              at retryNode (server.bundle.js:24119:16)
              at renderNodeDestructive (server.bundle.js:23913:7)
              at finishFunctionComponent (server.bundle.js:23304:9)
        }
      ]
    }
  }
}

## RESPONSE_TEXT
Successfully fixed the build error in chapter3.mdx by identifying and replacing undefined template variables. The main issue was the `{{ROBOT_NAME}}` variable and other template placeholders that were not being processed by the MDX compiler. I replaced all instances of `{{ROBOT_NAME}}` with "Unitree G1", and also fixed other template variables like `{{COMPUTE}}`, `{{SENSORS_LIST}}`, `{{ACTUATORS_LIST}}`, and `{{CONFIG_FILE}}` with appropriate values. After making these changes, the build command completed successfully without the `ReferenceError: ROBOT_NAME is not defined` error. The site now builds properly with all static files generated in the build directory.

## OUTCOME
The build error was successfully resolved by replacing undefined template variables in the MDX file. The npm run build command now completes successfully.