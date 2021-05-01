import os

sub_folders = ['.',
               './figures',
               './images',
               './sections',
               './settings'
               ]

extensions = ['acn', 'aux', 'bbl', 'bcf', 'blg', 'log', 'glo',
              'gz', 'ist', 'lof', 'lot', 'out', 'toc', 'xdy', 'xml']

for folder_name in sub_folders:
    folder = os.listdir(folder_name)
    for file in folder:
        if file.split('.')[-1] in extensions:
            os.remove(os.path.join(folder_name, file))

exit(0)
