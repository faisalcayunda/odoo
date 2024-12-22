from odoo import http
from odoo.http import request
import json

class RandomJobs(http.Controller):
    @http.route('/hr_refresh/random_jobs', type='http', auth='public', website=True)
    def get_random_jobs(self):
        Job = request.env['hr.job'].sudo()
        # Get 4 random published jobs
        random_jobs = Job.search([
            ('website_published', '=', True),
            ('state', '=', 'recruit')
        ], limit=4, order='random()')
        
        jobs_data = []
        for job in random_jobs:
            jobs_data.append({
                'id': job.id,
                'name': job.name,
                'department': job.department_id.name if job.department_id else '',
                'description': job.description[:200] + '...' if job.description else '',
                'url': f'/jobs/detail/{job.id}',
                'company': job.company_id.name if job.company_id else '',
                'location': job.address_id.city if job.address_id else '',
            })
        
        return request.make_response(
            json.dumps(jobs_data),
            headers=[('Content-Type', 'application/json')]
        )
