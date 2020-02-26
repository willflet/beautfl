project = 'TfL Transform'
copyright = '2020 William Fletcher'
author = 'Will Fletcher'

version = ''
release = '0.1'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'm2r'
]

autodoc_member_order = 'bysource'

source_suffix = ['.rst', '.md']
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = 'sphinx'

html_theme = 'cloud'
html_title = 'TfL Transform'
html_short_title = 'TfL Transform'
# html_theme_path = ['../../../../../../Websites/sphinx-themes',]
html_static_path = ['_static']
html_css_files = ['css/custom.css']
templates_path = ['_templates']
html_favicon = '_static/favicon.ico'
html_logo = '_static/logo.png'
htmlhelp_basename = 'docpages'

html_theme_options = dict(
    # restyles theme so page background is same as document
    borderless_decor = "false",
    # adds some slight gradients to headers & menu bars
    shaded_decor = "false",
    # uses lighter header & section styling
    lighter_header_decor = "false",
    nosidebar = "true",
    rightsidebar = "false",

    defaultcollapsed = "false",
    stickysidebar = "true",
    highlighttoc = "false",
    cleanup_toc = "false",

    # ms to spend scrolling when link to section on current page is clicked.
    # 0 to disable.
    smooth_scroll_links = "500",

    externalrefs = "true",
    externalicon = "&#187;",
    # issueicon = "\2727",
    # NOTE: would like to use sphinx's language setting,
    #       but doesn't seem to be available in templates.
    # hyphenation_language =

    # link targets
    # NOTE: roottarget can be name of document (eg: 'index', or "<toc>")
    #       logotarget is same, or can be "<root>" to reflect root value
    roottarget = "https://docs.bayesiansaddles.com/tfl-transform",
    logotarget = "<root>",

    # document dimensions
    # max width document will expand to.
    max_width = "11.5in",
    # max width of "minimal" mode (hides sidebar and other extras).
    minimal_width = "700px",
    # minimum size for large_screen_text_size to be used
    large_width = "16in",

    # min height of document
    min_height = "6in",

    # font sizes
    # base font size (% relative to browser default)
    default_layout_text_size = "100%",
    # optional base font size for screens larger than <minimal_width>
    minimal_layout_text_size = "75%",
    # optional base font size for screens bigger than <large_width>
    # large_layout_text_size =

    # font css url - for loading in fonts (eg google font dir)
    fontcssurl = "//fonts.googleapis.com/css?family=Lato|Noto+Serif",

    # styling for document body
    bodyfont = 'Lato, -apple-system, BlinkMacSystemFont, "Roboto", "Segoe UI", "Helvetica Neue", "Lucida Grande", Arial, sans-serif',
    bodytrimcolor = "rgba(0,0,0,.05)",
    bgcolor = "#ffffff",
    textcolor = "#222831",
    linkcolor = "#393e46",
    link_hover_text_color = "#081214",
    link_hover_bg_color = "#ffffff",
    link_hover_trim_color = "transparent",
    highlightcolor = "#eceef3",
    quotebgcolor = "rgba(0,0,0,.075)",
    quotetrimcolor = "rgba(0,0,0,.075)",
    codebgcolor = "#eceef3",
    codetextcolor = "#081214",
    codetrimcolor = "rgba(0,0,0,.075)",
    codevarfont = 'Monaco, Consolas, "Lucida Console", monospace',
    codeblockfont = 'Monaco, Consolas, "Lucida Console", monospace',
    bodylineheight = "1.5em",

    # styling for document headers
    headfont = '"Noto Serif", Georgia, Times, serif',
    headtextcolor = "#222831",
    headtrimcolor = "transparent",
    # headlinkcolor =
    # header_icon =

    # styling for section headers
    sectionbgcolor = "#eceef3",
    sectiontrimcolor = "rgba(0,0,0,.125)",
    sectiontextcolor = "#393e46",
    # TODO: rename this to childsectionbgcolor
    rubricbgcolor = "#92BCDE",
    section_radius = "3px",

    # admonitions
    inline_admonitions = "auto",
    admonition_note_color = "#E7F0FE",
    admonition_warning_color = "#ffe4e4",
    admonition_seealso_color = "#FFF7E0",
    admonition_deprecated_color = "#fbece0",
    admonition_todo_color = "#FFF7E0",
    admonition_trim_color = "rgba(0,0,0,.05)",
    admonition_trim_width = "1px 0",
    admonition_title_color = "rgba(0,0,0,.05)",
    admonition_size = "88%",
    admonition_radius = "3px",

    # objects
    # whether domain objects should get colored header
    colored_objects = "true",
    colored_object_prefixes = "nested",
    object_default_color = "#f0f0f0",
    object_class_color = "#f7c6dc",
    # object_exception_color = ,
    object_function_color = "#deebf5",
    object_attribute_color = "#e4eae2",
    object_trim_color = "rgba(0,0,0,0.1)",
    object_type_color = "rgba(0,0,0,0.3)",
    object_radius = "3px",
    object_header_prefix = "'<%- name %> \\2014\\0020'",

    # tables
    table_header_color = "rgba(0,0,0,.15)",
    table_shade_color = "rgba(0,0,0,.06)",
    table_trim_color = "rgba(0,0,0,.15)",

    # styling for footer / html background
    footerbgcolor = "#cad0d8",
    footertextcolor = "#393e46",

    # styling for sidebar
    sidebarwidth = "2.5in",
    # sidebar width used when document is greater than max width
    large_sidebar_width = "3in",
    sidebarbgcolor = "#fff",
    # small_sidebar_bg_color =
    sidebartextcolor = "#081214",
    sidebarlinkcolor = "#7b7e8e",
    sidebartrimcolor = "#rgba(0,0,0,.0)",
    sidebardetailcolor = "rgba(0,0,0,.0)",
    sidebarhighcolor = "#fff",
    sidebar_button_bg = "#eceef3",
    sidebar_link_hover_text_color = "#081214",
    sidebar_link_hover_bg_color = "#eceef3",
    sidebar_link_hover_trim_color = "transparent",

    # globaltoc: bg color for current page's LI
    # can also be set to special "section" value
    toc_local_bg_color = "default",

    # globaltoc: text color for current page's LI
    toc_local_text_color = "#081214",

    # globaltoc: trim color around current page's LI (defaults to toc_hover_trim_color)
    toc_local_trim_color = "default",

    # color for current section's TOC link (defaults to toc_hover_text_color)
    toc_current_text_color = "default",

    # override names used within sidebars
    # sidebar_master_title =
    # sidebar_root_title =
    sidebar_quicklinks_title = "Quick links",
    sidebar_localtoc_title = "Page contents",
    sidebar_prev_title = "Previous page",
    sidebar_next_title = "Next page",

    # styling for top & bottom relbars
    relbarbgcolor = "#081214",
    relbartextcolor = "#ffffff",
    relbarlinkcolor = "#ffffff",
    relbar_link_bg_color = "transparent",
    relbar_link_bg_hover = "#ffffff",

    # index page
    index_category_color = "#84ADBE",
)
