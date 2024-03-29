({
  "*": {
    "atom-ide-hyperclick": {
      darwinTriggerKeys: "shiftKey,altKey",
      linuxTriggerKeys: "shiftKey,altKey",
      win32TriggerKeys: "shiftKey,altKey"
    },
    "atom-ide-outline": {
      initialDisplay: false
    },
    "atom-ide-ui": {
      "atom-ide-datatip": {
        datatipDebounceDelay: 500
      },
      "atom-ide-terminal": {
        cursorBlink: true,
        fontFamily: "Source Code Pro, courier-new, courier, monospace"
      },
      use: {
        "atom-ide-diagnostics": "never",
        "atom-ide-diagnostics-ui": "never"
      }
    },
    "autocomplete-plus": {
      autoActivationDelay: 100,
      maxVisibleSuggestions: 20,
      minimumWordLength: 2,
      strictMatching: true
    },
    "autocomplete-python": {
      caseInsensitiveCompletion: false,
      useKite: false,
      useSnippets: "all"
    },
    autosave: {
      enabled: true
    },
    "bracket-matcher": {
      highlightMatchingLineNumber: true
    },
    core: {
      closeDeletedFileTabs: true,
      disabledPackages: ["archive-view", "buildium", "Chromo-Color-Previews", "image-view", "language-arduino", "language-c", "language-clojure", "language-csharp", "language-css", "language-gfm", "language-go", "language-java", "language-less", "language-lua", "language-make", "language-mustache", "language-objective-c", "language-perl", "language-php", "language-property-list", "language-python", "language-ruby-on-rails", "language-ruby", "language-rust-bundled", "language-sass", "language-shellscript", "language-sql", "language-todo", "language-toml", "language-typescript", "language-yaml", "minimap", "open-on-github", "package-generator", "pylint", "script", "spell-check", "atom-html-preview"],
      followSymlinks: false,
      ignoredNames: [".git", ".hg", ".svn", ".DS_Store", "._*", "Thumbs.db", "desktop.ini", ".idea"],
      openEmptyEditorOnStart: false,
      packagesWithKeymapsDisabled: ["atom-keyboard-macros", "custom-folds", "highlight-line", "git-diff", "language-markdown"],
      packagesWithSnippetsDisabled: ["MagicPython"],
      reopenProjectMenuCount: 50,
      restorePreviousWindowsOnStart: "no",
      telemetryConsent: "limited",
      themes: ["atom-dark-ui", "Chromodynamics"],
      uriHandlerRegistration: "always",
      useTreeSitterParsers: false
    },
    "custom-folds": {
      areRegionsFoldedOnLoad: true,
      areRegionsHighlighted: true,
      postfix_0: "fold here ⟰1⟰1⟰1",
      postfix_1: "fold here ⟰2⟰2⟰2",
      postfix_2: "fold here ⟰3⟰3⟰3",
      prefix_0: "fold here ⟱1⟱1⟱1",
      prefix_1: "fold here ⟱2⟱2⟱2",
      prefix_2: "fold here ⟱3⟱3⟱3"
    },
    editor: {
      autoIndentOnPaste: false,
      fontFamily: "Source Code Pro, Menlo, Consolas, DejaVu Sans Mono, monospace",
      lineHeight: 1.6,
      preferredLineLength: 500,
      scrollPastEnd: true,
      showIndentGuide: true,
      showInvisibles: true,
      softTabs: true,
      tabType: "soft"
    },
    "exception-reporting": {
      userId: "b54d002a-ce1e-4540-8755-e5d954f2ce78"
    },
    "file-watcher": {
      promptWhenChange: true
    },
    "find-and-replace": {
      autocompleteSearches: true,
      liveSearchMinimumCharacters: 2,
      projectSearchResultsPaneSplitDirection: "right",
      useRipgrep: true
    },
    "git-diff": {},
    "git-history": {
      maxCommits: 500
    },
    github: {
      showDiffIconGutter: true,
      viewChangesForCurrentFileDiffPaneSplitDirection: "right"
    },
    "highlight-line": {
      enableBackgroundColor: false,
      enableSelectionBorder: true,
      enableUnderline: true,
      hideHighlightOnSelect: true,
      underline: "dashed"
    },
    "highlight-selected": {
      highlightBackground: true,
      onlyHighlightWholeWords: false,
      showResultsOnScrollBar: true
    },
    "ide-python": {
      pylsPlugins: {
        autopep8: {
          enabled: false
        },
        flake8: {
          enabled: true,
          exclude: [".svn", "CVS", ".bzr", ".hg", ".git", "__pycache__", ".tox", ".eggs", "*.egg", ".idea", ".circleci"],
          maxLineLength: 500
        },
        jedi_definition: {
          follow_builtin_imports: true,
          follow_imports: true
        },
        mccabe: {
          threshold: 100
        },
        preload: {
          enabled: false
        },
        pycodestyle: {
          maxLineLength: 500
        },
        pydocstyle: {
          enabled: true
        },
        pylint: {},
        rope_completion: {},
        yapf: {
          enabled: true
        }
      },
      rope: {}
    },
    "iv-terminal": {
      defaultLocation: "right"
    },
    "linter-spell": {
      defaultLanguages: ["en es_any es_mx"],
      markdownWords: ["md", "uofp"],
      personalDictionaryPath: ".atom/personal.txt"
    },
    "linter-ui-default": {
      alwaysTakeMinimumSpace: true,
      panelHeight: 150,
      useBusySignal: false
    },
    "markdown-pdf": {
      format: "Legal",
      ghStyle: false
    },
    "markdown-writer": {
      fileExtension: ".md",
      relativeImagePath: true,
      tableAlignment: "left"
    },
    minimap: {
      adjustMinimapWidthToSoftWrap: false,
      autoToggle: false,
      ignoreWhitespacesInTokens: true,
      independentMinimapScroll: true,
      moveCursorOnMinimapClick: true
    },
    "nyan-indent": {
      color: "purple",
      customColors: {
        "0": "#990000",
        "1": "#990066",
        "2": "#995566",
        "3": "#996699",
        "4": "#880088"
      },
      opacity: 70,
      useCustomColors: true
    },
    "package-generator": {
      packageSyntax: "coffeescript"
    },
    "preview-plus": {
      htmlp: true,
      livePreview: true
    },
    "rainbow-delimiters": {
      delimiters: ["()", "[]", "{}", "\"\"", "''", "``", "“”", "‘’", "«»", "‹›"]
    },
    "rst-preview-pandoc": {
      pandocOpts: "-frst -thtml --webtex"
    },
    script: {
      cwdBehavior: "Directory of the script",
      stopOnRerun: true
    },
    "scroll-through-time": {
      direction: "up",
      modifierKey: "altKey"
    },
    "spell-check": {
      addKnownWords: true,
      enableDebug: true,
      grammars: ["source.asciidoc", "source.gfm", "text.git-commit", "text.plain", "text.plain.null-grammar", "source.rst", "text.restructuredtext", "text.md", "source.python"],
      locales: ["en-US"],
      useSystem: false
    },
    "split-diff": {
      hideDocks: true,
      turnOffSoftWrap: true
    },
    "sync-settings": {
      autoCheckForUpdatedBackup: "no",
      gistId: "f7219cfd5940e5c1761a2742bce379b2",
      hiddenSettings: {
        _lastBackupTime: "2021-07-11T23:06:22Z"
      },
      ignoreEol: true,
      installLatestVersion: true,
      personalAccessToken: "328a0526b069cc08de17d5df2e16e165c9cc5f9c"
    },
    "sync-settings-git-location": {
      gitUrl: "git@github.com:GaelicGrime/atomSync.git"
    },
    "tool-bar": {
      position: "Bottom"
    },
    "tool-bar-markdown-writer": {
      visibility: "showButtonsOnAll"
    },
    welcome: {
      showOnStartup: false
    },
    wrapperizer: {
      NewTextList: ["[%ST%](#%FT%)", "[%ST%](./fileOne.md#%FT%)", "%ST%2", "%ST%3", "%ST%4", "%ST%5", "%ST%6", "%ST%7", "%ST%8", "%ST%9", "%ST%A", "%ST%B", "%ST%C", "%ST%D", "%ST%E", "%ST%F", "%ST%G", "%ST%H", "if (%N%%T%%T%(%ST%%C%)%N%):%N%%T%# code", "%ST%J", "%ST%K", "%ST%L", "%ST%M", "%ST%N", "%ST%O", "%ST%P", "%ST%Q", "%ST%R", "%ST%S", "%ST%T", "%ST%U", "%ST%V", "%ST%W", "%ST%X", "%ST%Y", "%ST%Z"]
    }
  },
  ".console.python.text": {
    editor: {
      autoIndentOnPaste: false,
      preferredLineLength: 500,
      showIndentGuide: true,
      showInvisibles: true,
      softWrap: false,
      tabLength: 2,
      tabType: "soft"
    },
    "tabs-to-spaces": {
      onSave: "untabify"
    }
  },
  ".md.text": {
    editor: {
      autoIndentOnPaste: false,
      preferredLineLength: 200,
      showIndentGuide: true,
      showInvisibles: true,
      softWrap: true,
      softWrapHangingIndent: 4,
      tabLength: 2,
      tabType: "soft"
    },
    "tabs-to-spaces": {
      onSave: "untabify"
    }
  },
  ".python.regexp.source": {
    editor: {
      preferredLineLength: 500,
      tabLength: 2
    }
  },
  ".python.source": {
    editor: {
      autoIndentOnPaste: false,
      preferredLineLength: 500,
      showIndentGuide: true,
      showInvisibles: true,
      softWrap: false,
      tabLength: 2,
      tabType: "soft"
    },
    "tabs-to-spaces": {
      onSave: "untabify"
    }
  },
  ".python.text.traceback": {
    editor: {
      autoIndentOnPaste: false,
      preferredLineLength: 500,
      showIndentGuide: true,
      showInvisibles: true,
      softWrap: true,
      tabType: "soft"
    }
  }
});
