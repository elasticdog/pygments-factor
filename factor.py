class FactorLexer(RegexLexer):
    '''
    Lexer for Factor code.
    '''
    name = 'Factor'
    aliases = ['factor']
    filenames = ['*.factor']

    flags = re.UNICODE

    keywords = [
        '(accumulate)', '(all-integers?)', '(clone)', '(each-integer)',
        '(find-integer)', '*', '+', '+@', '+byte+', '+character+', '-', '-rot',
        '/', '/f', '/i', '/mod', '1array', '1sequence', '1string', '1vector',
        '2/', '2^', '2all?', '2array', '2bi', '2bi*', '2bi@', '2cache',
        '2cleave', '2cleave>quot', '2curry', '2dip', '2drop', '2dup', '2each',
        '2keep', '2map', '2map-as', '2map-reduce', '2nip', '2over', '2reduce',
        '2reverse-each', '2selector', '2sequence', '2tri', '2tri*', '2tri@',
        '2unclip-slice', '3append', '3append-as', '3array', '3bi', '3cleave',
        '3cleave>quot', '3curry', '3dip', '3drop', '3dup', '3each', '3keep',
        '3map', '3map-as', '3sequence', '3tri', '4array', '4dip', '4sequence',
        '<', '<=', '<array>', '<condition>', '<continuation>', '<enum>',
        '<flat-slice>', '<fp-nan>', '<repetition>', '<restart>', '<reversed>',
        '<slice>', '<string>', '<vector>', '<wrapper>', '=', '>', '>=',
        '>alist', '>array', '>bignum', '>boolean', '>continuation<', '>fixnum',
        '>float', '>integer', '>string', '>vector', '?', '?1+', '?at',
        '?execute', '?if', '?nth', '?push', 'abs', 'accumulate', 'accumulate!',
        'accumulate-as', 'align', 'alist>quot', 'all-integers?', 'all?', 'and',
        'any?', 'append', 'append!', 'append-as', 'array', 'array?', 'assert',
        'assert-sequence', 'assert-sequence=', 'assert-sequence?', 'assert=',
        'assert?', 'assoc', 'assoc-all?', 'assoc-any?', 'assoc-clone-like',
        'assoc-combine', 'assoc-diff', 'assoc-each', 'assoc-empty?',
        'assoc-filter', 'assoc-filter-as', 'assoc-find', 'assoc-hashcode',
        'assoc-intersect', 'assoc-like', 'assoc-map', 'assoc-map-as',
        'assoc-partition', 'assoc-refine', 'assoc-size', 'assoc-stack',
        'assoc-subset?', 'assoc-union', 'assoc=', 'assoc>map', 'assoc?', 'at',
        'at*', 'at+', 'attempt-all', 'attempt-all-error', 'attempt-all-error?',
        'bad-seek-type', 'bad-seek-type?', 'bi', 'bi*', 'bi-curry',
        'bi-curry*', 'bi-curry@', 'bi@', 'bignum', 'bignum?', 'binary-reduce',
        'bind', 'bit?', 'bitand', 'bitnot', 'bitor', 'bits>double',
        'bits>float', 'bitxor', 'bl', 'boa', 'boolean', 'boolean?', 'both?',
        'bounds-check', 'bounds-check?', 'bounds-error', 'bounds-error?',
        'build', 'but-last', 'but-last-slice', 'byte-array>bignum', 'cache',
        'call', 'call-effect', 'callcc0', 'callcc1', 'callstack',
        'callstack>array', 'callstack?', 'case', 'case-find', 'case>quot',
        'catchstack', 'change', 'change-at', 'change-global', 'change-nth',
        'check-slice', 'cleanup', 'clear', 'clear-assoc', 'cleave',
        'cleave>quot', 'clone', 'clone-like', 'collapse-slice', 'collector',
        'collector-for', 'complex', 'complex?', 'compose', 'compose?',
        'compute-restarts', 'concat', 'concat-as', 'cond', 'cond>quot',
        'condition', 'condition?', 'contents', 'continuation', 'continuation?',
        'continue', 'continue-with', 'copy', 'count', 'counter', 'curry',
        'curry?', 'cut', 'cut*', 'cut-slice', 'datastack', 'dec', 'delete-all',
        'delete-at', 'delete-at*', 'delete-slice', 'denominator', 'die', 'dip',
        'do', 'double>bits', 'drop', 'drop-prefix', 'dup', 'dupd', 'each',
        'each-block', 'each-index', 'each-integer', 'each-line', 'each-morsel',
        'each-stream-block', 'each-stream-line', 'either?', 'empty?', 'enum',
        'enum?', 'eq?', 'equal?', 'error', 'error-continuation',
        'error-stream', 'error-thread', 'even?', 'exchange', 'execute',
        'execute-effect', 'extract-keys', 'filter', 'filter!', 'filter-as',
        'find', 'find-from', 'find-integer', 'find-last', 'find-last-from',
        'find-last-integer', 'first', 'first2', 'first3', 'first4', 'fixnum',
        'fixnum?', 'flip', 'float', 'float>bits', 'float?', 'flush', 'follow',
        'fourth', 'fp-bitwise=', 'fp-infinity?', 'fp-nan-payload', 'fp-nan?',
        'fp-qnan?', 'fp-sign', 'fp-snan?', 'fp-special?', 'get', 'get-global',
        'global', 'glue', 'halves', 'harvest', 'hashcode', 'hashcode*', 'head',
        'head*', 'head-slice', 'head-slice*', 'head?', 'identity-hashcode',
        'identity-tuple', 'identity-tuple?', 'if', 'if*', 'if-empty',
        'if-zero', 'ifcc', 'ignore-errors', 'imaginary-part', 'immutable',
        'immutable-sequence', 'immutable-sequence?', 'immutable?', 'inc',
        'inc-at', 'index', 'index-from', 'indices', 'infimum',
        'init-namespaces', 'initialize', 'input-stream', 'insert-nth',
        'integer', 'integer?', 'interleave', 'iota', 'iota?', 'join', 'keep',
        'key?', 'keys', 'last', 'last-index', 'last-index-from', 'length',
        'lengthen', 'like', 'linear-case-quot', 'lines', 'log2',
        'log2-expects-positive', 'log2-expects-positive?', 'loop',
        'make-assoc', 'map', 'map!', 'map-as', 'map-find', 'map-find-last',
        'map-index', 'map-integers', 'map-reduce', 'map-sum', 'map>assoc',
        'max-length', 'maybe-set-at', 'member-eq?', 'member?', 'midpoint@',
        'min-length', 'mismatch', 'mod', 'most', 'move', 'namespace',
        'namestack', 'neg', 'new', 'new-assoc', 'new-like', 'new-resizable',
        'new-sequence', 'next-float', 'next-power-of-2', 'nip', 'nl',
        'no-case', 'no-case?', 'no-cond', 'no-cond?', 'not', 'nth', 'nths',
        'null', 'number', 'number=', 'number?', 'numerator', 'object', 'odd?',
        'off', 'on', 'or', 'output-stream', 'over', 'pad-head', 'pad-tail',
        'padding', 'pair', 'pair?', 'partition', 'pick', 'pop', 'pop*',
        'power-of-2?', 'prefix', 'prepend', 'prepose', 'prev-float', 'print',
        'produce', 'produce-as', 'product', 'push', 'push-all', 'push-at',
        'push-either', 'push-if', 'ratio', 'ratio?', 'rational', 'rational?',
        'read', 'read-partial', 'read-until', 'read1', 'readln', 'real',
        'real-part', 'real?', 'recip', 'recover', 'recursive-hashcode',
        'reduce', 'reduce-index', 'rem', 'remove', 'remove!', 'remove-eq',
        'remove-eq!', 'remove-nth', 'remove-nth!', 'rename-at', 'repetition',
        'repetition?', 'replace-slice', 'replicate', 'replicate-as',
        'resize-array', 'resize-string', 'rest', 'rest-slice', 'restart',
        'restart?', 'restarts', 'retainstack', 'rethrow', 'rethrow-restarts',
        'return', 'return-continuation', 'reverse', 'reverse!', 'reversed',
        'reversed?', 'rot', 'second', 'seek-absolute', 'seek-absolute?',
        'seek-end', 'seek-end?', 'seek-input', 'seek-output', 'seek-relative',
        'seek-relative?', 'selector', 'selector-for', 'sequence',
        'sequence-hashcode', 'sequence-hashcode-step', 'sequence=',
        'sequence?', 'set', 'set-at', 'set-catchstack', 'set-first',
        'set-fourth', 'set-global', 'set-last', 'set-length', 'set-namestack',
        'set-nth', 'set-second', 'set-third', 'sgn', 'shift', 'short',
        'shorten', 'shorter?', 'sift', 'slice', 'slice-error', 'slice-error?',
        'slice?', 'snip', 'snip-slice', 'spread', 'spread>quot', 'sq', 'start',
        'start*', 'stream-contents', 'stream-copy', 'stream-element-type',
        'stream-flush', 'stream-lines', 'stream-nl', 'stream-print',
        'stream-read', 'stream-read-partial', 'stream-read-until',
        'stream-read1', 'stream-readln', 'stream-seek', 'stream-tell',
        'stream-write', 'stream-write1', 'string', 'string?', 'subseq',
        'subseq?', 'substitute', 'suffix', 'suffix!', 'sum', 'sum-lengths',
        'supremum', 'surround', 'swap', 'swapd', 'tail', 'tail*', 'tail-slice',
        'tail-slice*', 'tail?', 'tell-input', 'tell-output', 'third',
        'thread-error-hook', 'throw', 'throw-restarts', 'times',
        'to-fixed-point', 'tri', 'tri*', 'tri-curry', 'tri-curry*',
        'tri-curry@', 'tri@', 'trim', 'trim-head', 'trim-head-slice',
        'trim-slice', 'trim-tail', 'trim-tail-slice', 'tuple', 'tuple?', 'u<',
        'u<=', 'u>', 'u>=', 'unclip', 'unclip-last', 'unclip-last-slice',
        'unclip-slice', 'unless', 'unless*', 'unless-empty', 'unless-zero',
        'unordered?', 'until', 'unzip', 'update', 'value-at', 'value-at*',
        'value?', 'values', 'vector', 'vector?', 'virtual-exemplar',
        'virtual-sequence', 'virtual-sequence?', 'virtual@', 'when', 'when*',
        'when-empty', 'when-zero', 'while', 'with', 'with-datastack',
        'with-input-stream', 'with-input-stream*', 'with-output-stream',
        'with-output-stream*', 'with-return', 'with-scope', 'with-streams',
        'with-streams*', 'with-variable', 'wrapper', 'wrapper?', 'write',
        'write1', 'wrong-values', 'wrong-values?', 'xor', 'zero?', 'zip'
    ]

    tokens = {
        'root': [
            # whitespace shouldn't matter
            (r'\s+', Text),

            # comments begin with ! or #!
            (r'(#)?!\s.*', Comment),

            # namespace
            (r'USING:[\w\W]*?;', Keyword.Namespace),
            (r'IN:\s.*', Keyword.Namespace),

            # word definitions
            (r'(GENERIC|MEMO|:)?:\s+\S+\s+(?=\(\s+)', Name.Function),
            (r'M:\s+\S+\s+\S+', Name.Function),
            (r'(ERROR||SYNTAX):\s+\S+', Name.Function),
            (r'\;', Name.Function),

            # stack declaration
            (r'(\()?\( .*--.* \)(\))?', Keyword.Type),

            # compiler directives
            (r'(inline|final|flushable|foldable|recursive)', Keyword.Declaration),

            # strings
            (r'(?s)"(\\\\|\\[0-7]+|\\.|[^"\\])*"', String.Double),
            (r'STRING:[\w\W]*?\n;', String.Heredoc),
            (r'CHAR:\s+\S+', String.Char),

            # constants
            (r'CONSTANT:\s+\S+', Name.Constant),

            # syntax
            (r'[\[{}()\]](?=\s)', Punctuation),
            (r'[BCHTVW]{', Punctuation),
            (r"'\[", Punctuation),

            # booleans
            (r'\b(t|f)\b', Name.Constant),

            # numbers
            (r'[+-]?\d+/\d+\b', Number),
            (r'[+-]?\d+\b', Number.Integer),
            (r'\b[+-]?\d*\.\d+([eE][-+]?\d+)?\b', Number.Float),
            (r'\bBIN:\s+[-+]?[01]+\b', Number),
            (r'\bHEX:\s+[-+]?[0-9a-fA-F]+\b', Number.Hex),
            (r'\bOCT:\s+[-+]?[0-7]+\b', Number.Oct),

            # keywords
            (r'\b(%s)' % '|'.join([
                re.escape(entry) + '\s' for entry in keywords ]),
                Keyword
            ),

            # everything else
            (r'\S+', Text),
        ]
    }
