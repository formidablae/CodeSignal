function newRoadSystem(roadRegister: boolean[][]): boolean {
    let rows: number[] = new Array(roadRegister.length).fill(0);
    let columns: number[] = new Array(roadRegister[0].length).fill(0);
    for (let i: number = 0; i < roadRegister.length; i++) {
        for (let j: number = 0; j < roadRegister[i].length; j++) {
            if (roadRegister[i][j]) {
                rows[i]++;
                columns[j]++;
            }
        }
    }
    for (let i: number = 0; i < rows.length; i++) {
        if (rows[i] !== columns[i]) {
            return false;
        }
    }
    return true;
}
