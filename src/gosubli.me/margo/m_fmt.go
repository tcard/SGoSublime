package main

import (
	"github.com/tcard/sgo/sgo/ast"
	"github.com/tcard/sgo/sgo/parser"
)

type mFmt struct {
	Fn        string
	Src       string
	TabIndent bool
	TabWidth  int
}

func (m *mFmt) Call() (interface{}, string) {
	res := M{}
	fset, af, err := parseAstFile(m.Fn, m.Src, parser.ParseComments)
	if err == nil {
		ast.SortImports(fset, af)
		res["src"], err = printSrc(fset, af, m.TabIndent, m.TabWidth)
	}
	return res, errStr(err)
}

func init() {
	registry.Register("fmt", func(b *Broker) Caller {
		return &mFmt{
			TabIndent: true,
			TabWidth:  8,
		}
	})
}
