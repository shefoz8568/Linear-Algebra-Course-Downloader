import subprocess
import sys

try:
    import requests
    from tqdm import tqdm
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', 'tqdm'])
    import requests
    from tqdm import tqdm

urls = [
    'http://www.archive.org/download/MIT18.06S05_MP4/01.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/02.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/03.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/04.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/05.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/06.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/07.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/08.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/09.mp4',
    'http://www.archive.org/download/MIT18.06S05_MP4/10.mp4',
    'http://www.archive.org/download/MIT18.06S10/pset1_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset10_s10_sol.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset2_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset3_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset4_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset5_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset6_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset7_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset8_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/pset9_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/exam1_s10.pdf',
    'http://www.archive.org/download/MIT18.06S10/exam1_s10_sol.pdf',
    'http://www.archive.org/download/MIT18.06S10/exam2_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/exam3_s10_soln.pdf',
    'http://www.archive.org/download/MIT18.06S10/exam3_s10.pdf',
    'http://www.archive.org/download/MIT18.06S10/Final_Answers.pdf',
    'http://www.archive.org/download/MIT18.06S10/Final_Exam.pdf'
]

def download_file(url):
    filename = url.split('/')[-1]
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        with open(filename, 'wb') as file:
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as bar:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)
                    bar.update(len(data))

for url in urls:
    try:
        download_file(url)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")
