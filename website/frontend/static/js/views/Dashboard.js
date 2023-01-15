import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
        this.setTitle("Dashboard");
    }

    async getHtml() {
        return `
            <h1>Nug Run Club 2023!</h1>
            <p>
                Watch this space! Here we'll put the current month pie with some graphs of current progress.       
            </p>
            <img src="images/pie.png" alt="Current Pie" style="width:600px;">
            <p>
                <a href="/posts" data-link>View previous month winners...</a>.
            </p>
        `;        
    }
}