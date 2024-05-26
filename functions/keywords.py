
vhdl_keywords = [
    "abs", "access", "after", "alias", "all", "and", "architecture", "array",
    "assert", "attribute", "begin", "block", "body", "buffer", "bus", "case",
    "component", "configuration", "constant", "context", "cover", "disconnect",
    "downto", "else", "elsif", "end", "entity", "exit", "file", "for", "force",
    "function", "generate", "generic", "group", "guarded", "if", "impure", "in",
    "inertial", "inout", "is", "label", "library", "linkage", "literal", "loop",
    "map", "mod", "nand", "new", "next", "nor", "not", "null", "of", "on", "open",
    "or", "others", "out", "package", "port", "postponed", "procedure", "process",
    "property", "protected", "pure", "range", "record", "register", "reject", "release",
    "rem", "report", "return", "rol", "ror", "select", "sequence", "severity",
    "shared", "signal", "sla", "sll", "sra", "srl", "subtype", "then", "to", "transport",
    "type", "unaffected", "units", "until", "use", "variable", "view", "vunit", "wait",
    "when", "while", "with", "xnor", "xor"
]

verilog_keywords = [
    "always", "and", "assign", "automatic", "begin", "buf", "bufif0", "bufif1",
    "case", "casex", "casez", "cell", "cmos", "config", "deassign", "default",
    "defparam", "design", "disable", "edge", "else", "end", "endcase", "endconfig",
    "endfunction", "endgenerate", "endmodule", "endprimitive", "endspecify",
    "endtable", "endtask", "event", "for", "force", "forever", "fork", "function",
    "generate", "genvar", "highz0", "highz1", "if", "ifnone", "incdir", "include",
    "initial", "inout", "input", "instance", "integer", "join", "large", "liblist",
    "library", "localparam", "macromodule", "medium", "module", "nand", "negedge",
    "nmos", "nor", "noshowcancelled", "not", "notif0", "notif1", "or", "output",
    "parameter", "pmos", "posedge", "primitive", "pull0", "pull1", "pulldown",
    "pullup", "pulsestyle_onevent", "pulsestyle_ondetect", "rcmos", "real", "realtime",
    "reg", "release", "repeat", "rnmos", "rpmos", "rtran", "rtranif0", "rtranif1",
    "scalared", "showcancelled", "signed", "small", "specify", "specparam", "strength",
    "strong0", "strong1", "supply0", "supply1", "table", "task", "time", "tran",
    "tranif0", "tranif1", "tri", "tri0", "tri1", "triand", "trior", "trireg", "unsigned",
    "use", "vectored", "wait", "wand", "weak0", "weak1", "while", "wire", "wor",
    "xnor", "xor"
]

c_keywords = [
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "inline", "int", "long", "register", "restrict", "return", "short",
    "signed", "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while", "_Alignas", "_Alignof",
    "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn",
    "_Static_assert", "_Thread_local"
]

cpp_keywords = [
    "alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel", "atomic_commit", 
    "atomic_noexcept", "auto", "bitand", "bitor", "bool", "break", "case", "catch", 
    "char", "char8_t", "char16_t", "char32_t", "class", "compl", "concept", "const", 
    "consteval", "constexpr", "constinit", "const_cast", "continue", "co_await", 
    "co_return", "co_yield", "decltype", "default", "delete", "do", "double", "dynamic_cast", 
    "else", "enum", "explicit", "export", "extern", "false", "float", "for", "friend", 
    "goto", "if", "inline", "int", "long", "mutable", "namespace", "new", "noexcept", 
    "not", "not_eq", "nullptr", "operator", "or", "or_eq", "private", "protected", 
    "public", "reflexpr", "register", "reinterpret_cast", "requires", "return", 
    "short", "signed", "sizeof", "static", "static_assert", "static_cast", "struct", 
    "switch", "synchronized", "template", "this", "thread_local", "throw", "true", 
    "try", "typedef", "typeid", "typename", "union", "unsigned", "using", "virtual", 
    "void", "volatile", "wchar_t", "while", "xor", "xor_eq"
]

tcl_keywords = [
    "after", "append", "apply", "array", "break", "catch", "cd", "close", "concat",
    "continue", "dict", "else", "elseif", "encoding", "eof", "error", "eval", "exec",
    "exit", "expr", "fblocked", "fconfigure", "fcopy", "file", "fileevent", "flush",
    "for", "foreach", "format", "gets", "glob", "global", "history", "if", "incr",
    "info", "interp", "join", "lappend", "lassign", "lindex", "linsert", "list",
    "llength", "load", "lrange", "lrepeat", "lreplace", "lreverse", "lsearch",
    "lset", "lsort", "namespace", "open", "package", "parray", "pid", "proc",
    "puts", "pwd", "read", "refchan", "regexp", "registry", "regsub", "rename",
    "return", "scan", "seek", "set", "socket", "source", "split", "string", "subst",
    "switch", "tailcall", "tcl::prefix", "tcl_endOfWord", "tcl_findLibrary",
    "tcl_startOfNextWord", "tcl_startOfPreviousWord", "tell", "throw", "time",
    "trace", "transchan", "try", "unset", "update", "uplevel", "upvar", "variable",
    "vwait", "while"
]

python_keywords = [
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", 
    "class", "continue", "def", "del", "elif", "else", "except", "finally", 
    "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", 
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
]

systemverilog_keywords = [
    "alias", "always", "always_comb", "always_ff", "always_latch", "and", "assert", 
    "assign", "assume", "automatic", "before", "begin", "bind", "bins", "binsof", 
    "bit", "break", "buf", "bufif0", "bufif1", "byte", "case", "casex", "casez", 
    "cell", "chandle", "class", "clocking", "cmos", "config", "const", "constraint", 
    "context", "continue", "cover", "covergroup", "coverpoint", "cross", "deassign", 
    "default", "defparam", "design", "disable", "dist", "do", "edge", "else", "end", 
    "endcase", "endclass", "endclocking", "endconfig", "endfunction", "endgenerate", 
    "endgroup", "endinterface", "endmodule", "endpackage", "endprimitive", 
    "endprogram", "endproperty", "endspecify", "endsequence", "endtable", "endtask", 
    "enum", "event", "expect", "export", "extends", "extern", "final", "first_match", 
    "for", "force", "foreach", "forever", "fork", "forkjoin", "function", "generate", 
    "genvar", "highz0", "highz1", "if", "iff", "ifnone", "ignore_bins", "illegal_bins", 
    "import", "incdir", "include", "initial", "inout", "input", "inside", "instance", 
    "int", "integer", "intersect", "join", "join_any", "join_none", "large", "liblist", 
    "library", "local", "localparam", "logic", "longint", "macromodule", "mailbox", 
    "matches", "medium", "modport", "module", "nand", "negedge", "new", "nmos", "nor", 
    "noshowcancelled", "not", "notif0", "notif1", "null", "or", "output", "package", 
    "packed", "parameter", "pmos", "posedge", "primitive", "priority", "program", 
    "property", "protected", "pull0", "pull1", "pulldown", "pullup", "pulsestyle_onevent", 
    "pulsestyle_ondetect", "pure", "rand", "randc", "rcmos", "real", "realtime", "ref", 
    "reg", "reject_on", "release", "repeat", "return", "rnmos", "rpmos", "rtran", 
    "rtranif0", "rtranif1", "scalared", "sequence", "shortint", "shortreal", 
    "showcancelled", "signed", "small", "solve", "specify", "specparam", "static", 
    "string", "strong0", "strong1", "struct", "super", "supply0", "supply1", "table", 
    "tagged", "task", "this", "throughout", "time", "timeprecision", "timeunit", 
    "tran", "tranif0", "tranif1", "tri", "tri0", "tri1", "triand", "trior", "trireg", 
    "type", "typedef", "union", "unique", "unsigned", "use", "uwire", "var", 
    "vectored", "virtual", "void", "wait", "wait_order", "wand", "weak0", "weak1", 
    "while", "wildcard", "wire", "with", "within", "wor", "xnor", "xor"
]

sh_keywords = [
    "if", "then", "else", "elif", "fi", "case", "esac", "for", "select", "while", 
    "until", "do", "done", "in", "function", "time", "coproc", "let", "matool"
]
