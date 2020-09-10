"use babel";

import { Range } from "atom";
import * as toml from "toml";

export function activate() {
	if(atom.packages.getAvailablePackageNames().indexOf("linter") < 0) {
		require("atom-package-deps").install();
	}
}

export function provideLinter() {
	return {
		name: "TOML Lint",
		scope: "file",
		lintsOnChange: false,
		grammarScopes: ["source.toml"],
		lint(editor) {
			try {
				toml.parse(editor.getText());
			} catch(error) {
				let line = error.line - 1;
				return [{
					severity: "error",
					excerpt: error.message,
					location: {
						file: editor.getPath(),
						position: new Range([line, error.column-1], [line, error.column])
					}
				}];
			}
			return [];
		}
	}
}
