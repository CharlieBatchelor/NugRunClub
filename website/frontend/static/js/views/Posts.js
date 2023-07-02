import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
        this.setTitle("Posts");
    }

    async getHtml() {
        return `
            <h2>Results of Last Month</h2>
            <p>
                This page shows the results from the previous month. Maybe add some tables,
                yearly progress etc...?       
            </p>
            <img src="images/lastMonthsPie.png" alt="Previous Pie" style="max-width: 100%; height: auto;">
            <p>
                <a href="/" data-link>Back to current month...</a>.
            </p>
        `;
    }
}