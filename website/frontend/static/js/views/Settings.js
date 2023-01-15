import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
        this.setTitle("Settings");
    }

    async getHtml() {
        return `
            <h1> Settings</h1>
            <p>
                Settings details.
            </p>
            <p>
                <a href="/" data-link>Back to Dashboard...</a>.
            </p>
        `;        
    }
}