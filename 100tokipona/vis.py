head = '''
<html>
<head>
   <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
   <title>Toki Pona UD Visualization</title>
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
   <link rel="stylesheet" type="text/css" href="https://universaldependencies.org/css/jquery-ui-redmond.css"/>
   <link rel="stylesheet" type="text/css" href="https://universaldependencies.org/css/style.css"/>
   <link rel="stylesheet" type="text/css" href="https://universaldependencies.org/css/style-vis.css"/>
   <script type="text/javascript" src="https://universaldependencies.org/lib/ext/head.load.min.js"></script>
</head>
<body>
<div id="main" class="center">
<div id="content">
<script type="text/javascript">
   console.time('loading libraries');
   var root = 'https://universaldependencies.org/'; // filled in by jekyll
   head.js(
                     // External libraries
                     // DZ: Copied from embedding.html. I don't know which one is needed for what, so I'm currently keeping them all.
                     root + 'lib/ext/jquery.min.js',
                     root + 'lib/ext/jquery.svg.min.js',
                     root + 'lib/ext/jquery.svgdom.min.js',
                     root + 'lib/ext/jquery.timeago.js',
                     root + 'lib/ext/jquery-ui.min.js',
                     root + 'lib/ext/waypoints.min.js',
                     root + 'lib/ext/jquery.address.min.js'
                  );
</script>
'''

tail = '''
<!-- support for embedded visualizations -->
<script type="text/javascript">
   var root = 'https://universaldependencies.org/'; // filled in by jekyll
   head.js(
                  // We assume that external libraries such as jquery.min.js have already been loaded outside!
                  // (See _layouts/base.html.)

                  // brat helper modules
                  root + 'lib/brat/configuration.js',
                  root + 'lib/brat/util.js',
                  root + 'lib/brat/annotation_log.js',
                  root + 'lib/ext/webfont.js',
                  // brat modules
                  root + 'lib/brat/dispatcher.js',
                  root + 'lib/brat/url_monitor.js',
                  root + 'lib/brat/visualizer.js',

                  // embedding configuration
                  root + 'lib/local/config.js',
                  // project-specific collection data
                  root + 'lib/local/collections.js',

                  // Annodoc
                  root + 'lib/annodoc/annodoc.js',

                  // NOTE: non-local libraries
                  'https://spyysalo.github.io/conllu.js/conllu.js'
               );

   var webFontURLs = [
                  //        root + 'static/fonts/Astloch-Bold.ttf',
                  root + 'static/fonts/PT_Sans-Caption-Web-Regular.ttf',
                  root + 'static/fonts/Liberation_Sans-Regular.ttf'
               ];

   var setupTimeago = function() {
                  jQuery("time.timeago").timeago();
               };

   head.ready(function() {
                  setupTimeago();

                  // mark current collection (filled in by Jekyll)
                  Collections.listing['_current'] = 'u-overview';

                  // perform all embedding and support functions
                  Annodoc.activate(Config.bratCollData, Collections.listing);
               });
</script>
</div>
</body>
</html>
'''


def load_lipu(file):
    lines = []
    with open(file) as f:
        for line in f:
            if line.startswith('###'):
                break
            line = line.strip()
            lines.append(line)
    xs = '\n'.join(lines).split('\n\n')
    xs = [x.strip() for x in xs]
    return xs


def to_conllu(lines):
    print('0\tROOT\t_\t_\t_\t_\t0\troot')
    for line in lines.split('\n'):
        if line.startswith('#'):
            continue
        line = line.split('\t')
        line = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                line[0],
                line[1],
                line[1],
                line[2],
                '_',
                '_',
                line[3],
                line[4])
        print(line)


def main():
    print(head)

    lipu = load_lipu('lipu.tsv')
    for x in lipu:
        print('<pre><code class="language-conllu">\n')
        to_conllu(x)
        print('</code></pre>\n')

    print(tail)

if __name__ == '__main__':
    main()

