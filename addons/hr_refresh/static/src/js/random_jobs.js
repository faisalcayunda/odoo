odoo.define('hr_refresh.random_jobs', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.RandomJobs = publicWidget.Widget.extend({
        selector: '.s_random_jobs',
        
        start: function () {
            this._loadRandomJobs();
            return this._super.apply(this, arguments);
        },

        _loadRandomJobs: function () {
            var self = this;
            $.get('/hr_refresh/random_jobs').then(function (data) {
                var $container = self.$('#random_jobs_container');
                $container.empty();

                data.forEach(function (job) {
                    var $jobCard = $(
                        `<div class="col-lg-3 col-md-6 mb-4">
                            <div class="card h-100 job-card">
                                <div class="card-body">
                                    <h5 class="card-title">${job.name}</h5>
                                    <h6 class="card-subtitle mb-2 text-muted">${job.department}</h6>
                                    <p class="card-text job-location">
                                        <i class="fa fa-map-marker"></i> ${job.location || 'Location not specified'}
                                    </p>
                                    <p class="card-text job-company">
                                        <i class="fa fa-building"></i> ${job.company}
                                    </p>
                                    <p class="card-text description">${job.description}</p>
                                </div>
                                <div class="card-footer">
                                    <a href="${job.url}" class="btn btn-primary">View Details</a>
                                </div>
                            </div>
                        </div>`
                    );
                    $container.append($jobCard);
                });
            });
        },
    });
});
