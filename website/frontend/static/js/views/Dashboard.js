import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
        this.setTitle("Dashboard");
    }

    async getHtml() {
        return `
            <h2>Nug Run Club 2023!</h2>
            <p>
                Watch this space! Here we'll put the current month pie with some graphs of current progress.       
            </p>
            <img src="images/pie.png" alt="Current Pie" style="max-width: 100%; height: auto; width: 80vw; max-height: 50vh;">
            <p>
                <a href="/posts" data-link>View previous month winners...</a>.
            </p>
        `;        
    }
}