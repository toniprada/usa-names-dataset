from os import listdir
from os.path import isfile, join

NAME_MIN_LENGTH = 3

def get_folder_files(folder, extension):
    return [join(folder,f) for f in listdir(folder)
        if isfile(join(folder,f)) and f.endswith(extension)]

print 'starting...'
names_set = set()
filenames = get_folder_files('names', '.txt')
for fn in filenames:
    with open(fn) as f:
        names = [line.split(',')[0] for line in f]
        names = [n for n in names if len(n)>NAME_MIN_LENGTH]
        names_set.update(names)

print len(names_set), 'unique names'
with open('names-dataset.txt', 'w+') as f:
    f.write('\n'.join(names_set).lower())
print 'file written'
print '...finished'

