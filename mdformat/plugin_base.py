#encoding=utf8
"""
Plugin base class and context object for the MD formatter.
"""

class MdContext:
    """Per-file processing state passed to all plugin hooks."""

    def __init__(self, fpath, fname, ftype, md5src,
                 is_md_file, is_src_file,
                 warn_cn_en_space, warn_title_space, warn_indent_space,
                 args):
        self.fpath = fpath
        self.fname = fname
        self.ftype = ftype
        self.md5src = md5src

        self.is_md_file = is_md_file
        self.is_src_file = is_src_file
        self.warn_cn_en_space = warn_cn_en_space
        self.warn_title_space = warn_title_space
        self.warn_indent_space = warn_indent_space

        # mutable per-line state
        self.codestate = False
        self.chartstate = False
        self.frontmatter = False
        self.frontmatter_count = 0

        # md-specific optional config read from frontmatter
        self.mdconfig = {}
        self.imgthumb = True

        self.errcnt = 0
        self.args = args  # dict of command-line flags

        # extra storage for plugins (keyed by plugin name)
        self._plugin_data = {}

    def plugin_state(self, key):
        """Return the mutable dict for a given plugin key."""
        if key not in self._plugin_data:
            self._plugin_data[key] = {}
        return self._plugin_data[key]

class MdPlugin:
    """
    Base class for MD formatter plugins.

    Override the hooks you need; default implementations are no-ops
    that pass data through unchanged.
    """

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def setup(self, args):
        """Called once at startup with the parsed args dict."""

    def teardown(self):
        """Called once after all files have been processed."""

    # ------------------------------------------------------------------
    # File-level hooks
    # ------------------------------------------------------------------

    def on_any_file(self, fpath, fname, ftype):
        """
        Called for every file before the source-type filter is applied.
        Return True to mark the file as handled and skip normal processing.
        """
        return False

    def should_skip_file(self, fpath, fname, ftype, ctx):
        """Return True to abort processing this file entirely."""
        return False

    def pre_process(self, fpath, fname, ftype, lines, ctx):
        """
        Called before the main line loop.
        Receives and must return the *lines* list (may be replaced).
        """
        return lines

    def post_process(self, fpath, fname, ftype, lines, ctx):
        """
        Called after the main line loop.
        Receives and must return the *lines* list (may be appended to etc.).
        """
        return lines

    def transform_page(self, page, fpath, fname, ftype, ctx):
        """
        Called on the full joined page string before writing.
        Receives and must return the page string.
        """
        return page

    # ------------------------------------------------------------------
    # Line-level hooks
    # ------------------------------------------------------------------

    def strip_line(self, line, ctx):
        """
        Called during the rstrip / normalisation phase (before checks).
        Return the (possibly modified) line.
        """
        return line

    def process_line(self, line, index, lines, ctx):
        """
        Called for each line inside the main loop.
        Return (new_line, errcnt_delta).
        """
        return line, 0
