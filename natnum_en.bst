%% Template:     Template LaTeX
%% Documento:    Archivo de estilos simple numerados [en]
%% Versión:      1.6 (23/08/2024)
%% Codificación: UTF-8
%%
%% Autor: Pablo Pizarro R.
%%        pablo@ppizarror.com
%%
%% Manual template: [https://latex.ppizarror.com]
%% Licencia MIT:    [https://opensource.org/licenses/MIT]

% -----------------------------------------------------------------------------
% VARIABLES GENERALES
% -----------------------------------------------------------------------------

ENTRY {
    address
    arxivId
    author
    booktitle
    chapter
    doi
    edition
    editor
    howpublished
    institution
    journal
    key
    month
    note
    number
    organization
    pages
    publisher
    school
    series
    title
    type
    url
    urldate
    volume
    year
}
{}
{
    label
}

INTEGERS {
    after.block
    after.quote
    after.quoted.block
    after.sentence
    before.all
    longest.label.width
    mid.sentence
    multiresult
    nameptr
    namesleft
    number.label
    numnames
    output.state
}

STRINGS {
    longest.label
    s
    t
}

% -----------------------------------------------------------------------------
% FUNCIONES UTILITARIAS
% -----------------------------------------------------------------------------

FUNCTION {and} {
    'skip$ {
        pop$ #0
    } if$
}

FUNCTION {not} {
    {
        #0
    }{
        #1
    } if$
}

FUNCTION {or} {
    {
        pop$ #1
    } 'skip$ if$
}

FUNCTION {blank.sep} {
    after.quote 'output.state :=
}

FUNCTION {either.or.check} {
    empty$
    'pop$ {
        "can't use both " swap$ * " fields in " * cite$ * warning$
    } if$
}

FUNCTION {emphasize} {
    duplicate$ empty$ {
        pop$ ""
    }{
        "{" swap$ * "}" *
    } if$
}

FUNCTION {empty.misc.check} {
    author empty$ title empty$ howpublished empty$
    month empty$ year empty$ note empty$
    and and and and and {
        "all relevant fields are empty in " cite$ * warning$
    } 'skip$ if$
}

FUNCTION {end.entry} {
    output.state after.quoted.block =
    'skip$
    'add.period$
    if$
    write$
    newline$
    "\backrefprint\backrefparscantrue" write$
    newline$
}

FUNCTION {field.or.null} {
    duplicate$ empty$ {
        pop$ ""
    } 'skip$ if$
}

FUNCTION {init.state.consts} {
    #0 'before.all :=
    #1 'mid.sentence :=
    #2 'after.quote :=
    #3 'after.sentence :=
    #4 'after.quoted.block :=
    #5 'after.block :=
}

FUNCTION {initialize.longest.label} {
    "" 'longest.label :=
    #1 'number.label :=
    #0 'longest.label.width :=
}

FUNCTION {longest.label.pass} {
    number.label int.to.str$ 'label :=
    number.label #1 + 'number.label :=
    label width$ longest.label.width > {
        label 'longest.label :=
        label width$ 'longest.label.width :=
    } 'skip$ if$
}

FUNCTION {multi.page.check} {
    't :=
    #0 'multiresult := {
        multiresult not
        t empty$ not
        and
    }{
        t #1 #1 substring$
        duplicate$ "-" =
        swap$ duplicate$ "," =
        swap$ "+" =
        or or {
            #1 'multiresult :=
        }{
            t #2 global.max$ substring$ 't :=
        } if$
    } while$
    multiresult
}

FUNCTION {n.dashify} {
    't := "" {
        t empty$ not
    }{
        t #1 #1 substring$ "-" = {
            t #1 #2 substring$ "--" = not {
                "--" *
                t #2 global.max$ substring$ 't :=
            }{
                {
                    t #1 #1 substring$ "-" =
                }{
                    "-" *
                    t #2 global.max$ substring$ 't :=
                } while$
            } if$
        }{
            t #1 #1 substring$ *
            t #2 global.max$ substring$ 't :=
        } if$
    } while$
}

FUNCTION {new.block} {
    output.state before.all = 'skip$ {
        output.state after.quote = {
            after.quoted.block 'output.state :=
        }{
            after.block 'output.state :=
        } if$
    } if$
}

FUNCTION {new.block.checka} {
    empty$
    'skip$
    'new.block
    if$
}

FUNCTION {new.block.checkb} {
    empty$
    swap$ empty$
    and
    'skip$
    'new.block
    if$
}

FUNCTION {new.sentence} {
    output.state after.block = 'skip$ {
        output.state before.all = 'skip$ {
            after.sentence 'output.state :=
        } if$
    } if$
}

FUNCTION {new.sentence.checka} {
    empty$
    'skip$
    'new.sentence
    if$
}

FUNCTION {output.bibitem} {
    newline$
    "\backrefparscanfalse" write$
    newline$
    "\bibitem{" write$ cite$ write$ "}" write$
    newline$
    ""
    before.all 'output.state :=
}

FUNCTION {output.links} {
    doi empty$ {
        arxivId empty$ {
            url empty$ {
                "" *
            }{
                ", \href{" * url * "} {\nolinkurl{\detokenize{" * url * "}}}" *
                urldate empty$ {
                    "" *
                }{
                    " (visited on " * urldate * ")" *
                } if$
            } if$
        }{
            ", \href{https://arxiv.org/abs/" * arxivId * "} {\nolinkurl{arXiv:\detokenize{" * arxivId * "}}}" *
        } if$
    }{
        ", \href{https://dx.doi.org/" * doi * "} {\nolinkurl{doi:\detokenize{" * doi * "}}}" *
    } if$
}

FUNCTION {output.nonnull} {
    's :=
    output.state mid.sentence = {
        ", " * write$
    }{
        output.state after.quote = {
            " " * write$
        }{
            output.state after.block = {
                add.period$ write$
                newline$
                "\newblock " write$
            }{
                output.state before.all = 'write$ {
                    output.state after.quoted.block = {
                        write$
                        newline$
                        "\newblock " write$
                    }{
                        add.period$ " " * write$
                    } if$
                } if$
            } if$
        } if$
        mid.sentence 'output.state :=
    } if$
    s
}

FUNCTION {output} {
    duplicate$ empty$
    'pop$
    'output.nonnull
    if$
}

FUNCTION {output.check} {
    't :=
    duplicate$ empty$ {
        pop$ "empty " t * " in " * cite$ * warning$
    } 'output.nonnull if$
}

FUNCTION {tie.or.space.connect} {
    duplicate$ text.length$ #3 < {
        "~"
    }{
        " "
    } if$
    swap$ * *
}

% -----------------------------------------------------------------------------
% FUNCIONES DE FORMATEO
% -----------------------------------------------------------------------------

FUNCTION {format.names} {
    's :=
    #1 'nameptr :=
    s num.names$ 'numnames :=
    numnames 'namesleft := {
        namesleft #0 >
    }{
        s nameptr "{vv~}{ll}{, jj}{, f.}" format.name$ 't :=
        nameptr #1 > {
            namesleft #1 > {
                ", " * t *
            }{
                "" *
                numnames #2 > {
                    "," *
                } 'skip$ if$
                t "others" = { 
                    " {\em et~al.}" *
                }{
                    " and " * t *
                } if$
            } if$
        } 't if$
        nameptr #1 + 'nameptr :=
        namesleft #1 - 'namesleft :=
    } while$
}

FUNCTION {format.addr.pub} {
    publisher empty$ {
        ""
    }{
        address empty$ {
            ""
        }{
            address ": " *
        } if$
        publisher *
    } if$
}

FUNCTION {format.article.crossref} {
    key empty$ {
        journal empty$ {
            "need key or journal for " cite$ * " to crossref " * crossref * warning$
            ""
        }{
            "in {" journal * "}" *
        } if$
    }{
        "in " key *
    } if$
    " \cite{" * crossref * "}" *
}

FUNCTION {format.authors} {
    author empty$ {
        ""
    }{
        author format.names
    } if$
}

FUNCTION {format.crossref.editor} {
    editor #1 "{vv~}{ll}" format.name$
    editor num.names$ duplicate$
    #2 > {
        pop$ " {\em et~al.}" *
    }{
        #2 < 'skip$ {
            editor #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" = {
                " {\em et~al.}" *
            }{
                " and " * editor #2 "{vv~}{ll}" format.name$ *
            } if$
        } if$
    } if$
}

FUNCTION {format.book.crossref} {
    volume empty$ {
        "empty volume in " cite$ * " to crossref " * crossref * warning$
        "In "
    }{
        "Vol.~" volume *
        " of " *
    } if$
    editor empty$
    editor field.or.null author field.or.null = or {
        key empty$ {
            series empty$ {
                "need editor, key, or series for " cite$ * " to crossref " * crossref * warning$
                "" *
            }{
                "{" * series * "}" *
            } if$
        }{
            key *
        } if$
    }{
        format.crossref.editor *
    } if$
    " \cite{" * crossref * "}" *
}

FUNCTION {format.btitle} {
    title emphasize
}

FUNCTION {format.bvolume} {
    volume empty$ {
        ""
    }{
        "vol.~" volume *
        series empty$
        'skip$ {
            " of " * series emphasize *
        } if$
        "volume and number" number either.or.check
    } if$
}

FUNCTION {format.pages} {
    pages empty$ {
        ""
    }{
        pages multi.page.check {
            "pp.~" pages n.dashify *
        }{
            "p.~" pages *
        } if$
    } if$
}

FUNCTION {format.chapter.pages} {
    chapter empty$ 'format.pages {
        type empty$ {
            "ch.~" chapter *
        }{
            type "l" change.case$ chapter tie.or.space.connect
        } if$
        pages empty$ 'skip$ {
            ", " * format.pages *
        } if$
    } if$
}

FUNCTION {format.date} {
    year empty$ {
        month empty$ {
            ""
        }{
            "there's a month but no year in " cite$ * warning$
            month
        } if$
    }{
        month empty$ {
            year
        }{
            month " " * year *
        } if$
    } if$
}

FUNCTION {format.edition} {
    edition empty$ {
        ""
    }{
        edition "l" change.case$ "~ed." *
    } if$
}

FUNCTION {format.editors} {
    editor empty$ {
        ""
    }{
        editor format.names
        editor num.names$ #1 > {
            ", eds." *
        }{
            ", ed." *
        } if$
    } if$
}

FUNCTION {format.in.ed.booktitle} {
    booktitle empty$ {
        ""
    }{
        "in " booktitle emphasize *
        editor empty$
        'skip$ {
            " (" * format.editors * ")" *
        } if$
    } if$
}

FUNCTION {format.incoll.inproc.crossref} {
    editor empty$
    editor field.or.null author field.or.null = or {
        key empty$ {
            booktitle empty$ {
                "need editor, key, or booktitle for " cite$ * " to crossref " * crossref * warning$
                ""
            }{
                "in {" booktitle * "}" *
            } if$
        }{
            "in " key *
        } if$
    }{
        "in " format.crossref.editor *
    } if$
    " \cite{" * crossref * "}" *
}

FUNCTION {format.number} {
    number empty$ {
        ""
    }{
        "no.~" number *
    } if$
}

FUNCTION {format.number.series} {
    volume empty$ {
        number empty$ {
            series field.or.null
        }{
            output.state mid.sentence = {
                "no.~"
            }{
                "No.~"
            } if$
            number *
            series empty$ {
                "there's a number but no series in " cite$ * warning$
            }{
                " in " * series *
            } if$
        } if$
    }{
        ""
    } if$
}

FUNCTION {format.paddress} {
    address empty$ {
        ""
    }{
        "(" address * ")" *
    } if$
}

FUNCTION {format.thesis.type} {
    type empty$
    'skip$ {
        pop$
        output.state after.block = {
            type "t" change.case$
        }{
            type "l" change.case$
        } if$
    } if$
}

FUNCTION {format.title} {
    title empty$ {
        ""
    }{
        "``" title "t" change.case$ * ",''" *
    } if$
}

FUNCTION {format.title.p} {
    title empty$ {
        ""
    }{
        "``" title "t" change.case$ * ".''" *
    } if$
}

FUNCTION {format.tr.number} {
    type empty$ {
        "Tech. Rep."
    } 'type if$
    number empty$ {
        "l" change.case$
    }{
        number tie.or.space.connect
    } if$
}

FUNCTION {format.volume} {
    volume empty$ {
        ""
    }{
        "vol.~" volume *
    } if$
}

% -----------------------------------------------------------------------------
% CONFIGURA CADA TIPO DE REFERENCIA
% -----------------------------------------------------------------------------

FUNCTION {article} {
    output.bibitem
    format.authors "author" output.check
    format.title "title" output.check
    blank.sep
    crossref missing$ {
        journal emphasize "journal" output.check
        format.volume output
        month empty$ {
            format.number output
        } 'skip$ if$
        format.pages output
        format.date "year" output.check
    }{
        format.article.crossref output.nonnull
        format.pages output
    } if$
    new.block
    note output
    end.entry
}

FUNCTION {book} {
    output.bibitem
    author empty$ {
        format.editors "author and editor" output.check
    }{
        format.authors output.nonnull
        crossref missing$ {
            "author and editor" editor either.or.check
        } 'skip$ if$
    } if$
    format.btitle "title" output.check
    crossref missing$ {
        format.bvolume output
        new.block
        format.number.series output
        format.addr.pub "publisher" output.check
    }{
        new.block
        format.book.crossref output.nonnull
    } if$
    format.edition output
    format.date "year" output.check
    new.block
    note output
    end.entry
}

FUNCTION {booklet} {
    output.bibitem
    format.authors output
    title empty$ {
        "empty title in " cite$ * warning$
        howpublished new.sentence.checka
    }{
        howpublished empty$ not
        address empty$ month empty$ year empty$ and and
        or {
            format.title.p output.nonnull
        }{
            format.title output.nonnull
        } if$
        blank.sep
    } if$
    howpublished output
    address output
    format.date output
    new.block
    note output
    end.entry
}

FUNCTION {inbook} {
    output.bibitem
    author empty$ {
        format.editors "author and editor" output.check
    }{
        format.authors output.nonnull
        crossref missing$ {
            "author and editor" editor either.or.check
        } 'skip$ if$
    } if$
    format.btitle "title" output.check
    crossref missing$ {
        format.bvolume output
        format.chapter.pages "chapter and pages" output.check
        new.block
        format.number.series output
        format.addr.pub "publisher" output.check
    }{
        format.chapter.pages "chapter and pages" output.check
        new.block
        format.book.crossref output.nonnull
    } if$
    format.edition output
    format.date "year" output.check
    new.block
    note output
    end.entry
}

FUNCTION {incollection} {
    output.bibitem
    format.authors "author" output.check
    format.title "title" output.check
    blank.sep
    crossref missing$ {
        format.in.ed.booktitle "booktitle" output.check
        format.bvolume output
        format.number.series output
        format.chapter.pages output
        format.addr.pub "publisher" output.check
        format.edition output
        format.date "year" output.check
    }{
        format.incoll.inproc.crossref output.nonnull
        format.chapter.pages output
    } if$
    new.block
    note output
    end.entry
}

FUNCTION {inproceedings} {
    output.bibitem
    format.authors "author" output.check
    format.title "title" output.check
    blank.sep
    crossref missing$ {
        format.in.ed.booktitle "booktitle" output.check
        format.bvolume output
        format.number.series output
        format.paddress output
        format.pages output
        organization output
        publisher output
        format.date "year" output.check
    }{
        format.incoll.inproc.crossref output.nonnull
        format.pages output
    } if$
    new.block
    note output
    end.entry
}

FUNCTION {conference} {
    inproceedings
}

FUNCTION {manual} {
    output.bibitem
    author empty$ {
        organization empty$ 'skip$ {
            organization output.nonnull
            address output
        } if$
    }{
        format.authors output.nonnull
    } if$
    format.btitle "title" output.check
    author empty$ {
        organization empty$ {
            address new.block.checka
            address output
        } 'skip$ if$
    }{
        organization address new.block.checkb
        organization output
        address output
    } if$
    format.edition output
    format.date output
    new.block
    note output
    end.entry
}

FUNCTION {mastersthesis} {
    output.bibitem
    format.authors "author" output.check
    format.title "title" output.check
    blank.sep
    "Master's thesis" format.thesis.type output.nonnull
    school "school" output.check
    address output
    format.date "year" output.check
    new.block
    note output
    end.entry
}

FUNCTION {misc} {
    output.bibitem
    format.authors output
    title empty$ {
        howpublished new.sentence.checka
    }{
        howpublished empty$ not
        month empty$ year empty$ and
        or {
            format.title.p output.nonnull
        }{
            format.title output.nonnull
        } if$
        blank.sep
    } if$
    howpublished output
    format.date output
    new.block
    note output
    end.entry
    empty.misc.check
}

FUNCTION {phdthesis} {
    output.bibitem
    format.authors "author" output.check
    format.btitle "title" output.check
    new.block
    "PhD thesis" format.thesis.type output.nonnull
    school "school" output.check
    address output
    format.date "year" output.check
    new.block
    note output
    end.entry
}

FUNCTION {proceedings} {
    output.bibitem
    editor empty$ {
        organization output
    }{
        format.editors output.nonnull
    } if$
    format.btitle "title" output.check
    format.bvolume output
    format.number.series output
    format.paddress output
    editor empty$ 'skip$ {
        organization output
    } if$
    publisher output
    format.date "year" output.check
    new.block
    note output
    end.entry
}

FUNCTION {techreport} {
    output.bibitem
    format.authors "author" output.check
    format.title "title" output.check
    blank.sep
    format.tr.number output.nonnull
    institution "institution" output.check
    address output
    format.date "year" output.check
    new.block
    note output
    end.entry
}

FUNCTION {unpublished} {
    output.bibitem
    format.authors "author" output.check
    format.title.p "title" output.check
    blank.sep
    note "note" output.check
    format.date output
    end.entry
}

% -----------------------------------------------------------------------------
% INICIA REFERENCIAS
% -----------------------------------------------------------------------------

FUNCTION {begin.bib} {
    preamble$ empty$ 'skip$ {
        preamble$ write$
        newline$
    } if$
    "\begin{thebibliography}{" longest.label * "}" * write$
    newline$
    "  \providecommand\backrefparscanfalse{}" write$
    newline$
    "  \providecommand\backrefparscantrue{}" write$
    newline$
    "  \providecommand\backrefprint{}" write$
    newline$
}

FUNCTION {default.type} {
    misc
}

FUNCTION {end.bib} {
    newline$
    "\end{thebibliography}" write$
    newline$
}

READ

EXECUTE {
    initialize.longest.label
}

ITERATE {
    longest.label.pass
}

EXECUTE {
    begin.bib
}

EXECUTE {
    init.state.consts
}

ITERATE {
    call.type$
}

EXECUTE {
    end.bib
}