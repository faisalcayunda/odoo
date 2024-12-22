/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class BitcoinChart extends Component {
    setup() {
        this._initChart();
    }

    /**
     * Initialize the Bitcoin price chart
     * @private
     */
    _initChart() {
        const ctx = this.el.querySelector('#bitcoinChart').getContext('2d');
        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Bitcoin Price (USD)',
                    data: [],
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
            }
        });
        this._fetchBitcoinData();
        // Update every 5 minutes
        setInterval(() => this._fetchBitcoinData(), 5 * 60 * 1000);
    }

    /**
     * Fetch Bitcoin price data from CoinGecko API
     * @private
     */
    _fetchBitcoinData() {
        fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
            .then(response => response.json())
            .then(data => {
                const price = data.bitcoin.usd;
                const now = new Date().toLocaleTimeString();
                
                // Update chart
                this.chart.data.labels.push(now);
                this.chart.data.datasets[0].data.push(price);
                
                // Keep only last 10 data points
                if (this.chart.data.labels.length > 10) {
                    this.chart.data.labels.shift();
                    this.chart.data.datasets[0].data.shift();
                }
                
                this.chart.update();
                
                // Update price display
                this.el.querySelector('#currentBitcoinPrice').textContent = `$${price.toLocaleString()}`;
                this.el.querySelector('#lastUpdated').textContent = now;
            })
            .catch(error => console.error('Error fetching Bitcoin price:', error));
    }

    /**
     * Clean up when component is destroyed
     */
    willUnmount() {
        if (this.chart) {
            this.chart.destroy();
        }
    }
}

BitcoinChart.template = 'bitcoin_tracker.BitcoinChart';
BitcoinChart.props = {};

registry.category("website_snippets").add("bitcoin_chart", {
    Component: BitcoinChart,
    selector: ".s_bitcoin_chart",
});
