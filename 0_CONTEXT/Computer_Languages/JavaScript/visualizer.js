/**
 * Visualization utilities for Active Inference JavaScript implementation
 */

export class Visualizer {
    constructor(config = {}) {
        this.config = {
            width: config.width || 800,
            height: config.height || 600,
            backgroundColor: config.backgroundColor || '#f0f0f0',
            textColor: config.textColor || '#333',
            gridColor: config.gridColor || '#ddd',
            beliefColors: config.beliefColors || ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7'],
            enableRealTime: config.enableRealTime || false,
            updateInterval: config.updateInterval || 100,
            showHistory: config.showHistory || true,
            maxHistoryPoints: config.maxHistoryPoints || 100,
            ...config
        };

        this.charts = new Map();
        this.dataBuffers = new Map();
        this.isRunning = false;
        this.animationFrame = null;

        // Initialize Chart.js if available
        this.chartJsAvailable = typeof Chart !== 'undefined';
        if (!this.chartJsAvailable) {
            console.warn('Chart.js not available. Some visualization features will be limited.');
        }
    }

    /**
     * Create a belief evolution chart
     */
    createBeliefChart(containerId, agent) {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error(`Container element with ID '${containerId}' not found`);
            return null;
        }

        if (!this.chartJsAvailable) {
            return this.createSimpleBeliefChart(container, agent);
        }

        const ctx = document.createElement('canvas');
        ctx.width = this.config.width;
        ctx.height = this.config.height;
        container.appendChild(ctx);

        const labels = [];
        const datasets = agent.getBeliefs().map((belief, index) => ({
            label: `State ${index}`,
            data: [belief],
            borderColor: this.config.beliefColors[index % this.config.beliefColors.length],
            backgroundColor: this.config.beliefColors[index % this.config.beliefColors.length] + '20',
            tension: 0.1,
            fill: false
        }));

        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: datasets
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 0 // Disable animations for real-time updates
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 1.0,
                        title: {
                            display: true,
                            text: 'Belief Probability'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Time Step'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Active Inference Belief Evolution',
                        font: { size: 16 }
                    },
                    legend: {
                        display: true,
                        position: 'top'
                    }
                }
            }
        });

        this.charts.set(containerId, chart);
        this.dataBuffers.set(containerId, {
            labels: [],
            datasets: datasets.map(() => [])
        });

        return chart;
    }

    /**
     * Create a simple belief chart without Chart.js
     */
    createSimpleBeliefChart(container, agent) {
        const canvas = document.createElement('canvas');
        canvas.width = this.config.width;
        canvas.height = this.config.height;
        container.appendChild(canvas);

        const ctx = canvas.getContext('2d');

        const chartData = {
            beliefs: agent.getBeliefs(),
            history: []
        };

        this.charts.set(container.id, {
            canvas: canvas,
            ctx: ctx,
            data: chartData,
            update: (newBeliefs) => {
                chartData.beliefs = newBeliefs;
                chartData.history.push([...newBeliefs]);
                if (chartData.history.length > this.config.maxHistoryPoints) {
                    chartData.history.shift();
                }
                this.drawSimpleBeliefChart(ctx, chartData);
            }
        });

        this.drawSimpleBeliefChart(ctx, chartData);
        return this.charts.get(container.id);
    }

    /**
     * Draw simple belief chart
     */
    drawSimpleBeliefChart(ctx, data) {
        const { width, height } = ctx.canvas;
        const { beliefs, history } = data;

        // Clear canvas
        ctx.fillStyle = this.config.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        // Draw grid
        ctx.strokeStyle = this.config.gridColor;
        ctx.lineWidth = 1;
        const gridSpacing = 50;
        for (let x = 0; x <= width; x += gridSpacing) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }
        for (let y = 0; y <= height; y += gridSpacing) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
        }

        // Draw belief bars
        const barWidth = width / (beliefs.length * 2);
        const maxBarHeight = height * 0.8;
        const startX = width * 0.1;

        beliefs.forEach((belief, index) => {
            const barHeight = belief * maxBarHeight;
            const x = startX + (index * barWidth * 2);
            const y = height - barHeight - 20;

            ctx.fillStyle = this.config.beliefColors[index % this.config.beliefColors.length];
            ctx.fillRect(x, y, barWidth, barHeight);

            // Draw label
            ctx.fillStyle = this.config.textColor;
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`State ${index}`, x + barWidth / 2, height - 5);
            ctx.fillText(`${(belief * 100).toFixed(1)}%`, x + barWidth / 2, y - 5);
        });

        // Draw title
        ctx.font = '16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Active Inference Belief Distribution', width / 2, 20);
    }

    /**
     * Update belief chart with new data
     */
    updateBeliefChart(containerId, newBeliefs) {
        const chart = this.charts.get(containerId);
        if (!chart) {
            console.error(`Chart for container '${containerId}' not found`);
            return;
        }

        if (this.chartJsAvailable && chart.config) {
            // Chart.js update
            const buffer = this.dataBuffers.get(containerId);
            buffer.labels.push(buffer.labels.length.toString());

            chart.data.datasets.forEach((dataset, index) => {
                dataset.data.push(newBeliefs[index]);
                if (dataset.data.length > this.config.maxHistoryPoints) {
                    dataset.data.shift();
                }
            });

            if (buffer.labels.length > this.config.maxHistoryPoints) {
                buffer.labels.shift();
            }

            chart.update('none'); // Disable animation for real-time updates
        } else if (chart.update) {
            // Simple chart update
            chart.update(newBeliefs);
        }
    }

    /**
     * Create free energy chart
     */
    createFreeEnergyChart(containerId, agent) {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error(`Container element with ID '${containerId}' not found`);
            return null;
        }

        if (!this.chartJsAvailable) {
            return this.createSimpleFreeEnergyChart(container);
        }

        const ctx = document.createElement('canvas');
        ctx.width = this.config.width;
        ctx.height = this.config.height;
        container.appendChild(ctx);

        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Free Energy',
                    data: [],
                    borderColor: '#e74c3c',
                    backgroundColor: '#e74c3c20',
                    tension: 0.1,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 0
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        title: {
                            display: true,
                            text: 'Free Energy'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Time Step'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Active Inference Free Energy Over Time',
                        font: { size: 16 }
                    }
                }
            }
        });

        this.charts.set(containerId, chart);
        return chart;
    }

    /**
     * Create simple free energy chart
     */
    createSimpleFreeEnergyChart(container) {
        const canvas = document.createElement('canvas');
        canvas.width = this.config.width;
        canvas.height = this.config.height;
        container.appendChild(canvas);

        const ctx = canvas.getContext('2d');

        const chartData = {
            values: [],
            maxValue: -Infinity,
            minValue: Infinity
        };

        this.charts.set(container.id, {
            canvas: canvas,
            ctx: ctx,
            data: chartData,
            update: (value) => {
                chartData.values.push(value);
                if (chartData.values.length > this.config.maxHistoryPoints) {
                    chartData.values.shift();
                }
                chartData.maxValue = Math.max(chartData.maxValue, value);
                chartData.minValue = Math.min(chartData.minValue, value);
                this.drawSimpleFreeEnergyChart(ctx, chartData);
            }
        });

        return this.charts.get(container.id);
    }

    /**
     * Draw simple free energy chart
     */
    drawSimpleFreeEnergyChart(ctx, data) {
        const { width, height } = ctx.canvas;
        const { values, maxValue, minValue } = data;

        // Clear canvas
        ctx.fillStyle = this.config.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        if (values.length < 2) return;

        // Calculate range
        const range = maxValue - minValue || 1;
        const padding = 40;
        const plotWidth = width - padding * 2;
        const plotHeight = height - padding * 2;

        // Draw axes
        ctx.strokeStyle = this.config.gridColor;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, height - padding);
        ctx.lineTo(width - padding, height - padding);
        ctx.stroke();

        // Draw grid lines
        ctx.lineWidth = 1;
        for (let i = 0; i <= 10; i++) {
            const y = padding + (i * plotHeight) / 10;
            ctx.beginPath();
            ctx.moveTo(padding, y);
            ctx.lineTo(width - padding, y);
            ctx.stroke();
        }

        // Draw data line
        ctx.strokeStyle = '#e74c3c';
        ctx.lineWidth = 2;
        ctx.beginPath();

        values.forEach((value, index) => {
            const x = padding + (index * plotWidth) / Math.max(values.length - 1, 1);
            const normalizedValue = (value - minValue) / range;
            const y = height - padding - (normalizedValue * plotHeight);

            if (index === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        });

        ctx.stroke();

        // Draw title
        ctx.fillStyle = this.config.textColor;
        ctx.font = '16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Active Inference Free Energy Over Time', width / 2, 20);

        // Draw current value
        if (values.length > 0) {
            const currentValue = values[values.length - 1];
            ctx.font = '12px Arial';
            ctx.fillText(`Current: ${currentValue.toFixed(4)}`, width - 100, 40);
        }
    }

    /**
     * Update free energy chart
     */
    updateFreeEnergyChart(containerId, freeEnergy) {
        const chart = this.charts.get(containerId);
        if (!chart) {
            console.error(`Chart for container '${containerId}' not found`);
            return;
        }

        if (this.chartJsAvailable && chart.config) {
            // Chart.js update
            chart.data.labels.push(chart.data.labels.length.toString());
            chart.data.datasets[0].data.push(freeEnergy);

            if (chart.data.labels.length > this.config.maxHistoryPoints) {
                chart.data.labels.shift();
                chart.data.datasets[0].data.shift();
            }

            chart.update('none');
        } else if (chart.update) {
            // Simple chart update
            chart.update(freeEnergy);
        }
    }

    /**
     * Create action distribution chart
     */
    createActionChart(containerId, nActions) {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error(`Container element with ID '${containerId}' not found`);
            return null;
        }

        if (!this.chartJsAvailable) {
            return this.createSimpleActionChart(container, nActions);
        }

        const ctx = document.createElement('canvas');
        ctx.width = this.config.width;
        ctx.height = this.config.height;
        container.appendChild(ctx);

        const chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Array.from({length: nActions}, (_, i) => `Action ${i}`),
                datasets: [{
                    label: 'Action Count',
                    data: Array(nActions).fill(0),
                    backgroundColor: this.config.beliefColors.slice(0, nActions),
                    borderColor: this.config.beliefColors.slice(0, nActions).map(color => color + 'ff'),
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 0
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Count'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Action'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Active Inference Action Distribution',
                        font: { size: 16 }
                    }
                }
            }
        });

        this.charts.set(containerId, chart);
        return chart;
    }

    /**
     * Create simple action chart
     */
    createSimpleActionChart(container, nActions) {
        const canvas = document.createElement('canvas');
        canvas.width = this.config.width;
        canvas.height = this.config.height;
        container.appendChild(canvas);

        const ctx = canvas.getContext('2d');

        const chartData = {
            counts: Array(nActions).fill(0),
            totalActions: 0
        };

        this.charts.set(container.id, {
            canvas: canvas,
            ctx: ctx,
            data: chartData,
            update: (action) => {
                chartData.counts[action]++;
                chartData.totalActions++;
                this.drawSimpleActionChart(ctx, chartData);
            }
        });

        this.drawSimpleActionChart(ctx, chartData);
        return this.charts.get(container.id);
    }

    /**
     * Draw simple action chart
     */
    drawSimpleActionChart(ctx, data) {
        const { width, height } = ctx.canvas;
        const { counts, totalActions } = data;

        // Clear canvas
        ctx.fillStyle = this.config.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        // Draw bars
        const barWidth = width / (counts.length * 2);
        const maxBarHeight = height * 0.7;
        const startX = width * 0.1;
        const maxCount = Math.max(...counts, 1);

        counts.forEach((count, index) => {
            const barHeight = (count / maxCount) * maxBarHeight;
            const x = startX + (index * barWidth * 2);
            const y = height - barHeight - 40;

            ctx.fillStyle = this.config.beliefColors[index % this.config.beliefColors.length];
            ctx.fillRect(x, y, barWidth, barHeight);

            // Draw label
            ctx.fillStyle = this.config.textColor;
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`Action ${index}`, x + barWidth / 2, height - 25);
            ctx.fillText(count.toString(), x + barWidth / 2, y - 5);

            // Draw percentage
            if (totalActions > 0) {
                const percentage = (count / totalActions * 100).toFixed(1);
                ctx.fillText(`${percentage}%`, x + barWidth / 2, height - 10);
            }
        });

        // Draw title
        ctx.font = '16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Active Inference Action Distribution', width / 2, 20);
    }

    /**
     * Update action chart
     */
    updateActionChart(containerId, action) {
        const chart = this.charts.get(containerId);
        if (!chart) {
            console.error(`Chart for container '${containerId}' not found`);
            return;
        }

        if (this.chartJsAvailable && chart.config) {
            // Chart.js update
            chart.data.datasets[0].data[action]++;
            chart.update('none');
        } else if (chart.update) {
            // Simple chart update
            chart.update(action);
        }
    }

    /**
     * Create comprehensive dashboard
     */
    createDashboard(containerId, agent) {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error(`Container element with ID '${containerId}' not found`);
            return null;
        }

        // Create dashboard structure
        container.innerHTML = `
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; padding: 20px;">
                <div id="belief-chart" style="width: 100%; height: 300px;"></div>
                <div id="free-energy-chart" style="width: 100%; height: 300px;"></div>
                <div id="action-chart" style="width: 100%; height: 300px;"></div>
                <div id="stats-panel" style="padding: 20px; background: #f8f9fa; border-radius: 8px;">
                    <h3>Agent Statistics</h3>
                    <div id="stats-content"></div>
                </div>
            </div>
        `;

        // Create charts
        this.createBeliefChart('belief-chart', agent);
        this.createFreeEnergyChart('free-energy-chart', agent);
        this.createActionChart('action-chart', agent.config?.nActions || 2);

        return {
            update: (newBeliefs, freeEnergy, action, agent) => {
                this.updateBeliefChart('belief-chart', newBeliefs);
                this.updateFreeEnergyChart('free-energy-chart', freeEnergy);
                this.updateActionChart('action-chart', action);
                this.updateStatsPanel(agent);
            }
        };
    }

    /**
     * Update statistics panel
     */
    updateStatsPanel(agent) {
        const statsContent = document.getElementById('stats-content');
        if (!statsContent) return;

        const stats = agent.getStatistics ? agent.getStatistics() : {};
        const beliefs = agent.getBeliefs();

        statsContent.innerHTML = `
            <p><strong>Steps:</strong> ${stats.totalSteps || 0}</p>
            <p><strong>Belief Entropy:</strong> ${stats.beliefEntropy?.toFixed(4) || 'N/A'}</p>
            <p><strong>Avg Free Energy:</strong> ${stats.averageFreeEnergy?.toFixed(4) || 'N/A'}</p>
            <p><strong>Current Beliefs:</strong></p>
            <ul>
                ${beliefs.map((belief, i) => `<li>State ${i}: ${(belief * 100).toFixed(1)}%</li>`).join('')}
            </ul>
        `;
    }

    /**
     * Start real-time visualization
     */
    startRealTime(agent, dashboardId) {
        if (this.isRunning) {
            console.warn('Real-time visualization already running');
            return;
        }

        this.isRunning = true;
        const dashboard = this.createDashboard(dashboardId, agent);

        const updateLoop = () => {
            if (!this.isRunning) return;

            // Generate random observation and step
            const observation = Math.floor(Math.random() * (agent.config?.nObservations || 3));
            const (action, freeEnergy) = agent.step(observation);
            const beliefs = agent.getBeliefs();

            // Update dashboard
            if (dashboard) {
                dashboard.update(beliefs, freeEnergy, action, agent);
            }

            // Schedule next update
            setTimeout(updateLoop, this.config.updateInterval);
        };

        updateLoop();
    }

    /**
     * Stop real-time visualization
     */
    stopRealTime() {
        this.isRunning = false;
    }

    /**
     * Export visualization as image
     */
    exportAsImage(containerId, filename = 'active_inference_viz.png') {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error(`Container element with ID '${containerId}' not found`);
            return;
        }

        // Use html2canvas if available, otherwise create simple export
        if (typeof html2canvas !== 'undefined') {
            html2canvas(container).then(canvas => {
                const link = document.createElement('a');
                link.download = filename;
                link.href = canvas.toDataURL();
                link.click();
            });
        } else {
            console.warn('html2canvas not available. Export functionality limited.');
            // Simple fallback - copy canvas content
            const canvases = container.querySelectorAll('canvas');
            if (canvases.length > 0) {
                const link = document.createElement('a');
                link.download = filename;
                link.href = canvases[0].toDataURL();
                link.click();
            }
        }
    }

    /**
     * Destroy all charts and clean up
     */
    destroy() {
        this.stopRealTime();

        for (const [containerId, chart] of this.charts.entries()) {
            if (this.chartJsAvailable && chart.destroy) {
                chart.destroy();
            } else if (chart.canvas) {
                chart.canvas.remove();
            }
        }

        this.charts.clear();
        this.dataBuffers.clear();
    }

    /**
     * Get chart data for external processing
     */
    getChartData(containerId) {
        const chart = this.charts.get(containerId);
        if (!chart) return null;

        if (this.chartJsAvailable && chart.config) {
            return {
                labels: chart.data.labels,
                datasets: chart.data.datasets.map(ds => ({
                    label: ds.label,
                    data: ds.data
                }))
            };
        } else if (chart.data) {
            return chart.data;
        }

        return null;
    }

    /**
     * Set chart configuration
     */
    setConfig(newConfig) {
        this.config = { ...this.config, ...newConfig };
    }

    /**
     * Get current configuration
     */
    getConfig() {
        return { ...this.config };
    }
}

// Create default visualizer instance
export const visualizer = new Visualizer();
