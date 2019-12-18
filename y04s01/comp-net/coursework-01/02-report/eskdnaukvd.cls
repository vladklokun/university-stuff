\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{eskdnaukvd}

% Passes class options to the underlying class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{eskdx}}
\ProcessOptions

% Load the ESKDX class
\LoadClass{eskdtext}

% XeTeX compatibility
\usepackage{xecyr}

%%% Redefine strings

% Change «Лит.» to «Літ.»
\renewcommand{\ESKDcolumnIVname}{%
  Літ.}

\renewcommand{\ESKDcolumnVname}{%
  Маса}

\renewcommand{\ESKDcolumnVIname}{%
  Масштаб}

\renewcommand{\ESKDcolumnVIIname}{%
  Аркуш}

\renewcommand{\ESKDcolumnVIItwosideName}{%
  Стор.}

\renewcommand{\ESKDcolumnVIIIname}{%
  Аркушів}

\renewcommand{\ESKDcolumnVIIItwosideName}{%
  Сторінок}

% Change «Розробив» to «Виконав».
\renewcommand{\ESKDcolumnXfIname}{%
  Виконав}

% Change «Перевірив» to «Керівник»
\renewcommand{\ESKDcolumnXfIIname}{%
  Керівник}

\renewcommand{\ESKDcolumnXfIIIname}{%
  Т. контр.}

\renewcommand{\ESKDcolumnXfIVname}{}

\renewcommand{\ESKDcolumnXfVname}{%
  Н. контр.}

% Change «Затвердив» «Зав. кафедри».
\renewcommand{\ESKDcolumnXfVIname}{%
  Зав. каф.}

\renewcommand{\ESKDcolumnXIVname}{%
  Зм.}

\renewcommand{\ESKDcolumnXVname}{%
  Лист}

\renewcommand{\ESKDcolumnXVIname}{%
  № докум.}
\renewcommand{\ESKDcolumnXVIIname}{%
  Підп.}
\renewcommand{\ESKDcolumnXVIIIname}{%
  Дата}
\renewcommand{\ESKDcolumnXIXname}{%
  Інв. № оригін.}
\renewcommand{\ESKDcolumnXXname}{%
  Підп. і дата}
\renewcommand{\ESKDcolumnXXIname}{%
  Взам. інв. №}
\renewcommand{\ESKDcolumnXXIIname}{%
  Інв. № дубл.}
\renewcommand{\ESKDcolumnXXIIIname}{%
  Підп. і дата}
\renewcommand{\ESKDcolumnXXIVname}{%
  Справ. №}
\renewcommand{\ESKDcolumnXXVname}{%
  Перш. заст.}
\renewcommand{\ESKDcolumnXXXIname}{%
  Копіював}
\@namedef{ESKDa0FormatName}{%
  Формат A0}
\@namedef{ESKDa1FormatName}{%
  Формат A1}
\@namedef{ESKDa2FormatName}{%
  Формат A2}
\@namedef{ESKDa3FormatName}{%
  Формат A3}
\@namedef{ESKDa4FormatName}{%
  Формат A4}
\@namedef{ESKDemptyFormatName}{%
  Формат\ \ \ \ }
\renewcommand{\ESKDcolumnXXXIIIname}{%
  Зона}

\renewcommand{\ESKDagreedName}{%
  Погоджено}
\renewcommand{\ESKDapprovingName}{%
  Затверджую}
\renewcommand{\ESKDapprovedName}{%
  Затверджено}
\renewcommand{\ESKDapprovingSheetName}{%
  Лист %
  затвердження}

\addto\captionsukrainian{%
  \def\tablename{{Таблиця}}%
  \def\figurename{{Рисунок}}%
  \def\refname{{Перелік 
    посилань}}}

\renewcommand{\ESKDspecColumnIname}{%
  Формат}
\renewcommand{\ESKDspecColumnIIname}{%
  Зона}
\renewcommand{\ESKDspecColumnIIIname}{%
  Поз.}
\renewcommand{\ESKDspecColumnIVname}{%
  Позначення}
\renewcommand{\ESKDspecColumnVname}{%
  Найменування}
\renewcommand{\ESKDspecColumnVIname}{%
  Кільк.}
\renewcommand{\ESKDspecColumnVIIname}{%
  Примітка}

\renewcommand{\ESKDspecIIcolumnIname}{\ESKDspecColumnIname}
\renewcommand{\ESKDspecIIcolumnIIname}{\ESKDspecColumnIIname}
\renewcommand{\ESKDspecIIcolumnIIIname}{\ESKDspecColumnIIIname}
\renewcommand{\ESKDspecIIcolumnIVname}{\ESKDspecColumnIVname}
\renewcommand{\ESKDspecIIcolumnVname}{\ESKDspecColumnVname}
\renewcommand{\ESKDspecIIcolumnVIname}{\ESKDspecColumnVIname}
\renewcommand{\ESKDspecIIcolumnVIIname}{%
  Маса}
\renewcommand{\ESKDspecIIcolumnVIIIname}{%
  Матеріал}
\renewcommand{\ESKDspecIIcolumnIXname}{\ESKDspecColumnVIIname}

\renewcommand{\ESKDchangeSheetName}{%
  Лист %
  реєстрації %
  змін}
\renewcommand{\ESKDchngColumnsIIhName}{%
  Номери аркушів %
  (сторінок)}
\renewcommand{\ESKDchngColumnIIname}{%
  змі\-не\-них}
\renewcommand{\ESKDchngColumnIIIname}{%
  за\-мі\-не\-них}
\renewcommand{\ESKDchngColumnIVname}{%
  но\-вих}
\renewcommand{\ESKDchngColumnVname}{%
  ану\-льо\-ва\-них}
\renewcommand{\ESKDchngColumnVIname}{%
  Разом аркушів %
  (сторінок) в докум.}
\renewcommand{\ESKDchngColumnVIIIname}{%
  Вхідний № %
  супровідного %
  докум. і %
  дата}

\def\@Asbuk#1{\ifcase#1\or
  А\orБ\orВ\orГ\orД\orЕ\or
  Ж\orІ\or
  К\orЛ\orМ\orН\orП\orР\or
  С\orТ\orУ\orФ\orХ\orЦ\or
  Ш\orЩ\orЮ\or
  Я\else{\@tempcnta \number #1\relax
      \advance\@tempcnta -24\relax
      \protect\number\@tempcnta}
  \fi}
\def\@asbuk#1{\ifcase#1\or
  а\orб\orв\orг\orд\orе\or
  ж\orі\or
  к\orл\orм\orн\orп\orр\or
  с\orт\orу\orф\orх\orц\or
  ш\orщ\orю\or
  я\else{\@tempcnta \number #1\relax
      \advance\@tempcnta -24\relax
      \protect\number\@tempcnta}
  \fi}
%%%

%%% NAU GOST Customisation

% Redefine the stamp
\newsavebox{\ESKD@stamp@ii@boxcustom}
\AtBeginDocument{%
\savebox{\ESKD@stamp@ii@boxcustom}{%
\setlength{\unitlength}{1mm}%
\begin{picture}(0,0)(0,0)
\linethickness{\ESKDlineThick}
\put(0,40){\line(1,0){185}}
% Remove thick line in left upper quadrant
% \put(0,30){\line(1,0){65}}
\put(0,25){\line(1,0){185}}
\put(135,20){\line(1,0){50}}
\put(135,15){\line(1,0){50}}
\linethickness{\ESKDlineThin}
% Remove thin lines in left upper quadrant
% \put(0,35){\line(1,0){65}}
\multiput(0,20)(0,-5){4}{\line(1,0){65}}
% Draw vertical lines
\linethickness{\ESKDlineThick}
\put(0,0){\line(0,1){40}}
% remove the vertical line 1 in left upper quadrant
% \put(7,25){\line(0,1){15}}
% Replace vertical line with shorter variant to vacate the left upper quadrant
% \put(17,0){\line(0,1){40}}
\put(17,0){\line(0,1){25}}
% \put(40,0){\line(0,1){25}}
\put(45,0){\line(0,1){25}}
\put(55,0){\line(0,1){25}}
\put(65,0){\line(0,1){40}}
\put(135,0){\line(0,1){25}}
\put(140,15){\line(0,1){5}}
\put(145,15){\line(0,1){5}}
\put(150,15){\line(0,1){10}}
\put(165,15){\line(0,1){10}}
\put(67, 1){\parbox[b][23mm][c]{66mm}{\centering\ESKDfontV\ESKDtheColumnI}}
\put(67, 26){\parbox[b][13mm][c]{106mm}{\centering\ESKDfontVII\ESKDtheColumnII}}
\put(135, 21.3){\makebox[15mm]{\ESKDfontIII\ESKDcolumnIVname}}
\put(135, 16.3){\makebox[5mm][c]{\ESKDfontIII\ESKDtheColumnIVfI}}
\put(140, 16.3){\makebox[5mm][c]{\ESKDfontIII\ESKDtheColumnIVfII}}
\put(145, 16.3){\makebox[5mm][c]{\ESKDfontIII\ESKDtheColumnIVfIII}}
\put(150, 21.3){\makebox[15mm]{\ESKDfontIII%
  \ifESKD@twoside\ESKDcolumnVIItwosideName\else\ESKDcolumnVIIname\fi}}
\put(165, 21.3){\makebox[20mm]{\ESKDfontIII%
  \ifESKD@twoside\ESKDcolumnVIIItwosideName\else\ESKDcolumnVIIIname\fi}}
\put(137, 1){\parbox[b][13mm][c]{46mm}{\centering\ESKDfontV\ESKDtheColumnIX}}
\put(0.5, 21.3){\makebox[16mm][l]{\ESKDfontIII\ESKDcolumnXfIname}}
\put(0.5, 16.3){\makebox[16mm][l]{\ESKDfontIII\ESKDcolumnXfIIname}}
\put(0.5, 11.3){\makebox[16mm][l]{\ESKDfontIII\ESKDcolumnXfIVname}}
\put(0.5, 6.3){\makebox[16mm][l]{\ESKDfontIII\ESKDcolumnXfVname}}
\put(0.5, 1.3){\makebox[16mm][l]{\ESKDfontIII\ESKDcolumnXfVIname}}
\put(17.5, 21.3){\makebox[22mm][l]{\ESKDfontIII\ESKDtheColumnXIfI}}
\put(17.5, 16.3){\makebox[22mm][l]{\ESKDfontIII\ESKDtheColumnXIfII}}
\put(17.5, 11.3){\makebox[22mm][l]{\ESKDfontIII\ESKDtheColumnXIfIV}}
\put(17.5, 6.3){\makebox[22mm][l]{\ESKDfontIII\ESKDtheColumnXIfV}}
\put(17.5, 1.3){\makebox[22mm][l]{\ESKDfontIII\ESKDtheColumnXIfVI}}
%\put(0, 26.3){\makebox[7mm]{\ESKDfontIII\ESKDcolumnXIVname}}
%\put(7, 26.3){\makebox[10mm]{\ESKDfontIII\ESKDcolumnXVname}}
%\put(17, 26.3){\makebox[23mm]{\ESKDfontIII\ESKDcolumnXVIname}}
%\put(40, 26.3){\makebox[15mm]{\ESKDfontIII\ESKDcolumnXVIIname}}
%\put(55, 26.3){\makebox[10mm]{\ESKDfontIII\ESKDcolumnXVIIIname}}
\end{picture}}}
\newcommand{\ESKD@stamp@ii@varcustom}{%
\begin{picture}(0,0)(0,0)
\ifESKD@enable@column@vii
  \put(150, 16.3){\makebox[15mm]{\ESKDfontIII\thepage}}
\fi
\ifESKD@enable@column@viii
  \put(165, 16.3){\makebox[20mm]{\ESKDfontIII\pageref{LastPage}}}
\fi
\end{picture}}

\newcommand{\ESKDdrawStampIIcustom}{%
  \put(\ESKDltu{\ESKDstampX},\ESKDltu{\ESKDstampY}){%
    \usebox{\ESKD@stamp@ii@boxcustom}}
  \put(\ESKDltu{\ESKDstampX},\ESKDltu{\ESKDstampY}){%
    \ESKD@stamp@ii@varcustom}}
%

% Create new style
\ESKDnewStyle{nausection}{40mm}
% Draw the frame
\ESKDputOnStyle{nausection}{frame}{\ESKDdrawFrame}
% Draw the stamp
\ESKDputOnStyle{nausection}{stamp}{\ESKDdrawStampIIcustom}

% Define the stamp
%% The box
\newsavebox{\ESKD@stamp@nauplain@a@box}
\AtBeginDocument{%
\savebox{\ESKD@stamp@nauplain@a@box}{%
\setlength{\unitlength}{1mm}%
\begin{picture}(0,0)(0,0)
% Horizontal lines
\linethickness{\ESKDlineThick}
\put(175,10){\line(1,0){10}}
% Vertical lines
\linethickness{\ESKDlineThick}
\put(175,0){\line(0,1){10}} % Page number line
\end{picture}}%
}
% The filling text
\newcommand{\ESKD@stamp@nauplain@a@var}{%
\begin{picture}(0,0)(0,0)
\ifESKD@enable@column@vii
  \put(175, 3){\makebox[10mm]{\thepage}}
\fi
\end{picture}}
\newcommand{\ESKDdrawStampNAUText}{%
  \put(\ESKDltu{\ESKDstampX},\ESKDltu{\ESKDstampY}){%
    \usebox{\ESKD@stamp@nauplain@a@box}}
  \put(\ESKDltu{\ESKDstampX},\ESKDltu{\ESKDstampY}){%
    \ESKD@stamp@nauplain@a@var}}

\ESKDnewStyle{nauplain}{10mm}
\ESKDputOnStyle{nauplain}{frame}{\ESKDdrawFrame}
\ESKDputOnStyle{nauplain}{stamp}{\ESKDdrawStampNAUText}
%%%

%%% Misc adjustments

% Define basic lengths
\setlength{\emergencystretch}{1em}
% \setlength{\parindent}{1.5em}

% Every section from new page

\usepackage{titlesec}
\newcommand{\sectionbreak}{\clearpage}
\titlespacing{\section}{\parindent}{\baselineskip}{\baselineskip}
\titlespacing{\subsection}{\parindent}{\baselineskip}{\baselineskip}
\titlespacing{\subsubsection}{\parindent}{\baselineskip}{\baselineskip}

\ESKDsectAlign{section}{Center}
\ESKDsectStyle{section}{\normalsize\bfseries%\MakeTextUppercase
}
\ESKDsectSkip{section}{0pt}{0pt}

\ESKDsectAlign{subsection}{Center}
\ESKDsectStyle{subsection}{\normalsize\bfseries%\MakeTextUppercase
}
\ESKDsectSkip{subsection}{0pt}{0pt}

\ESKDsectAlign{subsubsection}{Center}
\ESKDsectStyle{subsubsection}{\normalsize\bfseries%\MakeTextUppercase
}
\ESKDsectSkip{subsubsection}{0pt}{0pt}

%%% Set up captions
\RequirePackage{caption}

\usepackage{caption}
\usepackage{subcaption}

%\DeclareCaptionLabelFormat{closing}{#2)}
%\captionsetup[subtable]{labelformat = closing}

%\captionsetup[subfigure]{labelformat = closing}

\captionsetup[table]{
  aboveskip = 0\baselineskip,
  belowskip = 0\baselineskip,
  labelsep = period,
  justification = raggedleft,
}

\captionsetup[figure]{
  aboveskip = 1\baselineskip,
  belowskip = 0\baselineskip,
  labelsep = period,
  justification = centering,
}

\captionsetup[subfigure]{
  labelformat = simple,
  labelformat = brace,
  justification = RaggedRight,
  singlelinecheck = false,
  labelsep = period,
}

% Change caption counters
\usepackage{chngcntr}
\counterwithin{table}{section}
\counterwithin{figure}{section}
%%%

%%% Support Ragged typesetting
\usepackage{ragged2e}
%%%

%%% Set up tables
% Ragged columns
\usepackage{array}
\newcolumntype{v}[1]{>{\RaggedRight\arraybackslash\hspace{0pt}}p{#1}}
\newcolumntype{b}[1]{>{\Centering\arraybackslash\hspace{0pt}}p{#1}}
\newcolumntype{n}[1]{>{\RaggedLeft\arraybackslash\hspace{0pt}}p{#1}}
%%%

%%% Custom commands
\newcommand{\allcaps}[1]{%
  {%
    \addfontfeatures{%
      Letters = UppercaseSmallCaps,
      LetterSpace = 8,%
    }%
    #1%
  }%
}
\newcommand{\filename}[1]{\texttt{#1}}
\newcommand{\progname}[1]{\texttt{#1}}
\newcommand{\commandname}[1]{\texttt{#1}}
\newcommand{\modulename}[1]{\texttt{#1}}
\newcommand{\transeng}[1]{{англ.}~\textit{\textenglish{#1}}}
%%%

%%% Framing code listings
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
\tcbuselibrary{minted}
\tcbuselibrary{skins}

\newminted[codegeneric]{text}{%
  autogobble,%
  style=bw,%
  breaklines,%
  fontsize=\small,%
}

% Text file listing
\newtcblisting[
  auto counter,
  list inside,
  number within = section,
]{listingplaintext}[3][]{%
  minted language = text,
  minted style    = bw,
  minted options  = {
    autogobble,
		% linenos,
    tabsize = 4,
    breaklines,
    breakanywhere,
    fontsize = \footnotesize,
  },
  empty,
  sharp corners,
  coltitle = black,
  borderline horizontal = {1pt}{0pt}{black},
  titlerule = {0.5pt},
  titlerule style = {
    black,
  },
  toptitle = 0.3em,
  bottomtitle = 0.3em,
  before skip      = \intextsep,
  after  skip      = \intextsep,
  title            = {Лістинг \thetcbcounter: #2},
  list entry       = {\protect\numberline{\thetcbcounter}#2},
  left = 0em,
  right = 0em,
  %
  listing only,
  breakable,
  %
  label = {#3},%
}

\newtcbinputlisting[
  use counter from = listingplaintext,
  list inside,
  number within = section
]{\inputplaintext}[4][]{%
  minted language = text,
  minted style    = bw,
  minted options  = {
    autogobble,
    linenos,
    tabsize = 4,
    breaklines,
    breakanywhere,
    fontsize = \footnotesize,
  },
  empty,
  sharp corners,
  coltitle = black,
  borderline horizontal = {1pt}{0pt}{black},
  titlerule = {0.5pt},
  titlerule style = {
    black,
  },
  toptitle = 0.3em,
  bottomtitle = 0.3em,
  before skip      = \intextsep,
  after  skip      = \intextsep,
  title            = {Лістинг \thetcbcounter: #3},
  list entry       = {\protect\numberline{\thetcbcounter}#3},
  left = 0em,
  right = 0em,
  %
  listing file={#2},
  listing only,
  breakable,
  %
  label = {#4}
}
