
import subprocess
def run_mapreduce_job(request):
    # Run Hadoop MapReduce job
    try:
        subprocess.run([
            'hadoop', 'jar', '/path/to/hadoop-streaming.jar',
            '-input', '/epharmacy/medicines.csv',
            '-output', '/epharmacy/output',
            '-mapper', '/path/to/mapper.py',
            '-reducer', '/path/to/reducer.py'
        ], check=True)
        return JsonResponse({'status': 'MapReduce job completed'})
    except subprocess.CalledProcessError as e:
        return JsonResponse({'status': 'MapReduce job failed', 'error': str(e)})
        
def get_mapreduce_results():
    try:
        result = subprocess.check_output(['hadoop', 'fs', '-cat', '/epharmacy/output/part-00000'])
        return [line.split("\t") for line in result.decode('utf-8').strip().split("\n")]
    except Exception as e:
        return []

def analytics(request):
    trends = get_mapreduce_results()
    return render(request, 'dashboard/analytics.html', {'trends': trends})


