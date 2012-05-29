def removeRotamers(pdblist):
	#Just Remove all rotamers other than the first.
	pdb_prime = [pdblist[0]]
	for residue in pdblist[1:]:
		lastAtom = pdb_prime[-1][12:16]
		lastChain_and_Res = pdb_prime[-1][21:27]
		
		if residue[12:16] == lastAtom and residue[21:27] == lastChain_and_Res: #Then it's a rotamer.
			continue #throw it out
		else:
			pdb_prime.append(residue)
			continue

	return pdb_prime

def getPolymerAtoms(pdb,chain=None):
	modreslist = [l for l in pdb if l[0:6] == "MODRES"]
	modresdict = dict()
	for modres in modreslist:
		splitup = modres.split()
		modresdict[(splitup[3],splitup[4])] = splitup
	
	pdb = [l for l in pdb if l.startswith("ATOM") or (l.startswith("HETATM") and modresdict.has_key((l[21], l[22:26].strip())))]

	if chain:
		pdb = [i for i in pdb if i[21] == chain]
	return pdb
