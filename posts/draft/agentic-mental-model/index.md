---
title: "Agentic Mental Model"
abstract: |
  The most profound shift in software engineering isn't a new language, framework, or cloud service. It's the transition from writing code to expressing intent, and trusting intelligent systems to translate that intent into working software. Writing code for the sake of writing code has never been the point of software engineering, it is about creating a solution to human problems. Software engineering is **more** than just writing code.
draft: true
---

## What is Agentic?

Before diving into a mental model for agentic development, let's first consider what an agentic system actually is. Software development provides one of the most advanced examples: an approach in which autonomous AI agents plan, write, test, and modify code with minimal human intervention.

Agentic coding does not eliminate software engineering, but rather moves engineering effort from producing and implementing code to designing the environment in which implementations can be produced, tested, and trusted.

Every agent is built from five parts:
1. **The model** is the reasoning engine. It comes from [Large Language Model](https://en.wikipedia.org/wiki/Large_language_model), **LLM**. It reads the current context, decides what should happen next, and produces the next thought, tool call, or message.
2. **Tools** connects the model to the world with API calls, code execution, databases, and other agents it can delegate to.
3 **Memory**, or context window, allows the agent to recall past interactions, retrieve project-specific rules, and retain context across sessions.
4. **Orchestration** is the code that runs the loop. It assembles context for each model call, dispatches tool calls, captures results, and decides whether to continue.
5. **Deployment** is what turns the prototype into a service: hosting, identity, observability, and production infrastructure.

## A New Paradigm

A new paradigm, in which developers express *what* they want to build rather than *how* to build it, has emerged. Rather than following a strict chronological eras that replace one after another, we should think as **different levels of abstraction**. Indeed autocomplete, chat, synchronous agents, background agents, and autonomous workflows continue to coexist and varies accros industries.

### Level 1: Autocompletion

The first generation was accelerated autocomplete. Tools, like [Github Copilot in 2021](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/), predicted the next line, filled in boilerplate, and saved keystrokes on repetitive patterns. Even though the feature is useful and genuinely time-saving, the workflow stayed identical. Software engineers wrote code, ran it, debug, and repeat. AI tool assisted by reducing friction.

![](assets/GitHub-Copilot_blog-header.webp){width=200}

### Level 2: Collaboration

The second generation introduced synchronous agents where you described a task, in natural language, and the model generates the code for you. [Andrej Karpathy](https://karpathy.ai/) said "The hottest new programming language is English". It perfectly encapsulate this era of interaction back and forth between a genrative Ai chatbot and a user. After the model generated code, you then reviewed it, corrected it, and finally iterated toward a working result.

This step moved further up the stack of delegation. There are ess typing than the previous level and it is more about describing intent. But you are still present for every step. The agent is a _collaborator_, not an autonomous worker. You hold the overall context, directe the next move, and catch mistakes in real time.

<blockquote class="twitter-tweet" data-lang="en" data-theme="dark"><p lang="en" dir="ltr">The hottest new programming language is English</p>&mdash; Andrej Karpathy (@karpathy) <a href="https://x.com/karpathy/status/1617979122625712128?ref_src=twsrc%5Etfw">January 24, 2023</a></blockquote> <script async src="https://platform.x.com/widgets.js" charset="utf-8"></script>

:::{.callout-note collapse=false title="Side notes on Vibe Coding"}
#### What is Vibe Coding

Two years after aanoncing that English is the hotest programming language, Andrej Karpathy coined the term, **vibe coding**, where you "fully give in to the vibes, embrace exponentials, and forget that the code even exists."

<blockquote class="twitter-tweet" data-theme="dark"><p lang="en" dir="ltr">There&#39;s a new kind of coding I call &quot;vibe coding&quot;, where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It&#39;s possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper…</p>&mdash; Andrej Karpathy (@karpathy) <a href="https://x.com/karpathy/status/1886192184808149383?ref_src=twsrc%5Etfw">February 2, 2025</a></blockquote> <script async src="https://platform.x.com/widgets.js" charset="utf-8"></script>

Vibe coding emphasizes the significance of AI tools and their increasing capabilities. It is a fresh take in coding where users express their intention using plain text or speech and AI transforms that thinking into executable code. The goal of vibe coding is to create an AI powered development environment where AI agents serve as coding assistants making suggestions in real time, automating tedious processes and even producing standard codebase structures.

By prioritizing experimentation before refining structure and performance, vibe coding embraces a "code first, refine later" mindset. This opens opportunities for developers to prioritize building first and optimizing later. Inline with agile framework, specifically the principle of fast-prototyping, iterative development and cyclical feedback loops; vibe coding allows developpers to focus on these principles while churning out protoypes by eliminating.

#### Limitations of vibe coding

Vibe coding is undoubtedly potent however it has some technical and real world challenges. Here are some of the key challenges listed:
1. **Technical complexity**: Vibe coding can handle basic standard frameworks but for real world applications where technical requirements can be novel or complex, vibe coding becomes challenging.
2. **Code quality and performance issues**: Vibe coding is helpful to test applications and create prototypes, but it still requires optimization and refinement to make sure that the code quality is maintained. Vibe coding is not an ideal choice for distributed applications because it requires structured level architecture and sophisticated optimization strategies.
3. **Debugging challenges**: Code generated by AI is challenging to debug because it's dynamic and lacks architectural structure.
4. **Maintenance and updates**: Many times, if the software application is not updated in a timely manner, it becomes outdated which is why they require regular maintenance as well as updates. Applications built using AI generated code face maintenance and update challenges if the code structure is not properly maintained. This can cause developers to struggle to understand the underlying logic when trying to keep it updated and optimized.
5. **Security concerns**: This limitation is the most critical as it can lead to several risks and extreme vulnerabilities. Code generated using AI is often excluded from code reviews and security checks, leading to unseen vulnerabilities that can go unnoticed and be exploited.

### Level 3: Delegation ... the third generation: Agentic Workflow

The third generation introduced **autonomous agents**. These agents can take a specification and run with it for thirty minutes, an hour, several hours and increasingly days. They set up environments, install dependencies, write tests, hit failures, research solutions online, fix the failures, write the implementation, test it again, set up services, and produce artifacts you can review.

You hand them a task, move on to something else, and come back to logs, previews, and pull requests. You are no longer interacting line by line. You are defining outcomes and reviewing results. Now, fully autonomous agents can clone repositories, plan multi-file changes, execute them in sandboxed environments, run tests, and submit pull requests: all without a human typing a single line of code.

### Level 4: Orchestration

You could even add a fourth level, the orchestration era where swarms of agents and even self-improving agents come into play. A human or coordinating system decomposes work across multiple agents, routes results through verification, and manages dependencies between tasks.

> Autonomy is not binary. It is a transfer of control over increasingly large portions of the development loop.


------------- CONTINUE -----------------------------

## The Factory and Its Operator

### The factory is the system

> Explain specifications, harnesses, agents, tests, guardrails, and delivery pipelines.

https://addyosmani.com/blog/factory-model/
The most useful mental model for this new paradigm is that you are no longer just writing code. You are building the factory that builds your software.

That factory consists of fleets of agents. Each agent has a task, a toolbelt (repositories, test runners, deployment scripts, documentation), context (specs, architecture decisions, prior constraints), and a feedback loop. Instead of hand-holding a single agent through a single task, you spin up many agents in parallel. One handles backend refactors. Another implements a feature. Another writes integration tests. Another updates documentation. You review outputs, give feedback, refine specs, and redeploy.

The analogy runs deeper than it might first appear. A factory has quality control. A factory has process documentation. A factory has inputs that need to be precisely specified or the outputs come out wrong. A factory stalls when the environment is unreliable. All of these properties map directly onto agentic software development, and taking the analogy seriously points you toward the investments that actually matter.

Inside teams that have adopted this model aggressively, a substantial portion of merged pull requests now originate from agents running autonomously in cloud environments. That is not theoretical anymore. It is production reality for a growing number of engineering organizations.

The sentiments from Cursor around “The developer’s job is becoming building the system that builds the software, the factory, not just the product” and “reviewing ideas is a lot more fun than reviewing code” (video) resonate with these points.

The mental model that ties these transformations together is the **factory model**.
In this model, the developer's primary output is not code: it's **the system that
produces code**. This system includes:

- Specifications and context that define what needs to be built
- Agents that translate specifications into implementation
- Tests and quality gates that verify correctness
- Feedback loops that route failures back to agents for correction
- Guardrails that constrain agents to safe, predictable behavior

A factory manager does not assemble every widget by hand. They design the assembly
line and ensure quality control. Success comes from giving agents **success
criteria rather than step-by-step instructions**, then letting them iterate.

```{mermaid}
%%| label: fig-factory-model
%%| fig-cap: "The Factory Model — Developer designs the system, agents produce the code, tests verify the output"
flowchart TD
    Dev["👨‍💻 Developer\n(Factory Manager)"]

    subgraph Factory["🏭 The Factory"]
        direction TB
        Spec["📋 Specifications\n& Context"] --> Agents["🤖 AI Agents\n(Implementation)"]
        Agents --> Tests["✅ Tests\n& Quality Gates"]
        Tests --> FL["🔄 Feedback\nLoops"]
        FL --> Agents
        GR["🛡️ Guardrails\n& Constraints"] --> Agents
    end

    Dev --> Factory
    Factory --> Code["📦 Production\nCode"]

    style Factory fill:#1a1a2e,stroke:#4a4a8a,color:#fff
    style Dev fill:#533483,stroke:#7a5ab5,color:#fff
    style Code fill:#1a3d1a,stroke:#4a8a4a,color:#fff
```

### The orchestrator coordinates the system

> Explain decomposition, delegation, dependency management, monitoring, and escalation.

The developer's evolving role:
conductors and orchestrators
As AI takes over more of the implementation work, the developer's role is transforming in
ways that are both exciting and disorienting. We find it useful to think of two modes that
developers move between fluidly: conductor and orchestrator.12

The conductor: hands-on, real-time direction
In conductor mode, a developer works in real-time with an AI pair-programmer. They're in
the IDE, watching code appear, guiding the AI with prompts and corrections, and maintaining
fine-grained control over what gets written. The AI is a powerful instrument, but the
developer is actively directing every movement.

This mode is typical when working on complex logic, debugging tricky issues, or working in
unfamiliar codebases where the developer needs to understand each change as it's made.
Tools like GitHub Copilot, Google's Gemini Code Assist, Cursor, and Windsurf primarily
support this mode through inline completions, chat interfaces, and edit-in-place capabilities.
The conductor mode is natural for developers who come from traditional engineering
backgrounds. It preserves the sense of understanding and control that many engineers value.
The risk is that it can also become a bottleneck - if the developer is personally directing every
keystroke, the throughput improvement from AI is limited.
The orchestrator: async, multi-agent delegation
In orchestrator mode, the developer operates at a higher level of abstraction. They
define goals, assign them to agents, and review results - but they're not watching code
appear line by line. Agents may be working in the background, in parallel, on different
parts of a codebase. The developer checks in periodically, reviews output, and provides
course corrections.
This mode is typical for well-defined tasks like bug fixes, feature implementations against
established patterns, codebase migrations, and test generation. Tools like Google's Jules,
GitHub Copilot's agent mode, Cursor's background agents, and Claude Code support this
mode through async task execution, often working in sandboxed environments with full
access to the repository, build tools, and test suites.13
The orchestrator mode requires a different skill set. Instead of deep expertise in syntax and
language idioms, it demands strong skills in:
• Specification: Defining tasks precisely enough that an agent can execute them
without ambiguity

Decomposition: Breaking large tasks into appropriately sized units for agent execution
• Evaluation: Quickly assessing whether agent output meets quality standards
• System design: Designing the constraints, tests, and feedback loops that keep
agents productive

#### Role transition

There's an uncomfortable truth here: _orchestrating_ agents feels a lot like
management: delegating tasks, reviewing output, redirecting when things go
sideways,etc. If you became an engineer because you didn't want to be a manager,
this shift might feel like a betrayal. The role changed underneath you.

=> https://addyosmani.com/blog/future-agentic-coding/

### The developer moves between conductor and orchestrator modes

> Explain synchronous supervision versus asynchronous delegation.

### Orchestration can itself be automated

> Explain machine orchestration while preserving human judgment and accountability.

#### The bottleneck becomes verification

> Explain why generating more code or running more agents does not automatically create more valuable software.





## Practical Patterns

1. Agent-first drafts with tight iteration loops

  Don’t use AI for one-off suggestions. Generate entire first drafts, then
  refine. The Claude Code team practice: have the model review its own code
  with a fresh context window. This catches issues before human review.

2. Declarative communication

  Spend 70% of effort on problem definition, 30% on execution. Write
  comprehensive specs, define success criteria, provide test cases up front.
  Guide the agent’s goals, not its methods.

3. Automated verification

  If you repeatedly fix the same class of mistake, write a test or lint rule
  preemptively. Make the agent explain its code and flag potential problems
  before you review.













-----------------
## A New Software Development Life Cycle (SDLC)

The software development life cycle has already been through one major
transformation. Over the past two decades, most enterprises moved from sequential
waterfall processes to iterative models: Agile sprints, continuous integration,
DevOps pipelines, and rapid release cycles.

**AI compresses this cycle dramatically, but unevenly:** implementation that once
took weeks can now be done in hours, while requirements, architecture, and
verification remain stubbornly human-paced.

### The Factory Model


### The Pareto Law

= https://addyo.substack.com/p/the-80-problem-in-agentic-coding

Andrej Karpathy Twitter / X

= Boris Cherney :
> “Pretty much 100% of our code is written by Claude Code + Opus 4.5. For me
> personally it has been 100% for two+ months now, I don’t even make small edits
> by hand. I shipped 22 PRs yesterday and 27 the day before, each one 100%
> written by Claude. I think most of the industry will see similar stats in the
> coming months - it will take more time for some vs others.”


...WIP...

Let AI do 80% of the work and focus your energy on the 20% left.

The 80% Problem

A persistent challenge: AI agents can rapidly generate approximately **80% of
the code** for a feature, but the remaining 20% — edge cases, error handling,
integration points, and subtle correctness requirements — demands deep contextual
knowledge that current models often lack.

The nature of AI errors has evolved from simple syntax mistakes to more insidious
**conceptual failures**: wrong assumptions about business logic, missing edge
cases, and architectural decisions that create subtle long-term maintenance
burdens. These errors are harder to detect because the code "looks right" and may
even pass basic tests.

::: {.callout-tip}
The developers who navigate this challenge most effectively use AI for what it's
good at (rapid implementation of well-specified tasks) while reserving their own
attention for what AI struggles with (ambiguous requirements, architectural
trade-offs, and correctness verification).
:::

## Where to Start

::: {.panel-tabset}
### For Individual Developers

1. **Set up an `AGENTS.md`** for the project. Start with ten lines: stack,
   conventions, hard rules, workflow. Add a rule every time the agent does
   something it should not do again.

2. **Install a set of skills** for your coding agents (like Agents CLI) to build,
   evaluate, deploy and optimize agents.

3. **Pick one repetitive workflow and make it the first agent.** A research
   workflow, a code review process, a recurring report. Use a coding agent for
   the prototype, graduate it to a production agent when it earns its keep.
   Building one agent end to end teaches more than reading about a hundred.

4. **Write the tests and evals before generating the code.** Together they are
   the contract with the AI. A well-written test and eval suite communicates
   intent more precisely than any natural-language prompt, and turns AI-assisted
   development from vibe coding into agentic engineering.

5. **Review every line the agent produces that is going to ship.** Be skeptical
   of anything that looks clever. Check imports for real packages. Verify that
   error handling covers realistic failure modes.

6. **Maintain your developer skills.** AI handles the routine so the developer
   can focus on the challenging. That arrangement only works if foundational
   skills — debugging, system design, intuition for performance and correctness
   — stay sharp.

### For Engineering Leaders

1. **Make context engineering a first-class engineering practice.** Treat
   `AGENTS.md`, system prompts, eval suites, and skill libraries as code:
   reviewed in pull requests, versioned with the project, owned by named
   engineers.

2. **Set the bar at the eval, not the demo.** A working demo proves an agent can
   succeed once. A passing eval suite proves it succeeds reliably. Define what
   you are scoring: task success, tool use quality, trajectory compliance,
   hallucination, and response quality.

3. **Re-shape code review for AI-generated code.** Extra attention to
   hallucinated dependencies, inadequate error handling, and subtle correctness
   gaps that look right at a glance.

4. **Distinguish prototyping work from production work in team norms.** Vibe
   coding is the right speed for exploration. Agentic engineering is the right
   discipline for production. Make the boundary explicit.

5. **Invest in harness components as a shared team asset.** Reusable system
   prompts, skill libraries, MCP server connections, and evaluation harnesses
   compound across projects. Treat them as infrastructure.

### For Organizations

1. **Treat AI-assisted development as an engineering investment, not a
   productivity feature.** Rolling out a coding agent without eval coverage,
   observability, and clear architectural standards produces speed without
   quality.

2. **Invest in the production substrate before scale.** What graduates a
   vibe-coded prototype to production is operations discipline: trajectory and
   final-response evals in CI, traces of every agent run, scoped permissions,
   and security review tuned to generated code's failure modes.

3. **Adopt open standards.** Model Context Protocol (MCP) for tool access and
   Agent2Agent (A2A) for cross-agent delegation are converging into the
   connective tissue of multi-agent systems.

4. **Plan for hybrid teams of humans and agents.** The strongest production
   results come from architectures where humans set direction, agents do the
   implementation, and clear handoff protocols govern the boundary.

5. **Reframe hiring and skill development around judgment, not just
   implementation.** The most valuable engineers in the next several years will
   be the ones who can direct agents well, not the ones who can write the most
   code.
:::


------- #######    TO REVIEW    ########----------------
    An AI agent is a software system that perceives a goal, plans steps to reach
    it, takes actions through tools, observes the results, and iterates until
    the goal is met or it hits a stopping condition. Where a chatbot produces a
    response and waits for the next prompt, an agent runs its own loop. You give
    it a goal at the top, then it decides what to do next at each step.
