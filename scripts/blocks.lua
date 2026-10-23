-- Keep examples, propositions, figures, and exercise numbering consistent.
function Div(el)
  local c=el.classes[1]
  local latex=FORMAT:match('latex')
  if c=='figure' then
    local key=el.attributes.key
    local f=io.open('src/figure-data/'..key..'.tex'); local tikz=f:read('*a');f:close()
    local f2=io.open('src/figure-data/'..key..'.txt');local cap=f2:read('*a');f2:close()
    if latex then return pandoc.RawBlock('latex','\\begin{figure}[htbp]\\centering\n\\resizebox{.98\\linewidth}{!}{'..tikz..'}\n\\caption{'..cap..'}\\end{figure}') end
    return pandoc.RawBlock('html','<figure><img src="../assets/fig-'..key..'.svg" alt="'..cap..'" loading="lazy"><figcaption>'..cap..'</figcaption></figure>')
  elseif c=='example' or c=='proposition' then
    local title=el.attributes.title or ''
    if latex then
      local b={pandoc.RawBlock('latex','\\begin{'..c..'}['..title..']')}
      for _,v in ipairs(el.content) do table.insert(b,v) end
      table.insert(b,pandoc.RawBlock('latex','\\end{'..c..'}')); return b
    end
    table.insert(el.content,1,pandoc.Para({pandoc.Strong({pandoc.Str((c=='example' and 'Example. ' or 'Proposition. ')..title)})}))
    return el
  elseif c=='exercises' and latex then
    local b={pandoc.RawBlock('latex','\\begin{exercises}')}
    for _,v in ipairs(el.content) do
      if v.t=='OrderedList' then
        for _,item in ipairs(v.content) do
          table.insert(b,pandoc.RawBlock('latex','\\item '));for _,x in ipairs(item) do table.insert(b,x) end
        end
      else table.insert(b,v) end
    end
    table.insert(b,pandoc.RawBlock('latex','\\end{exercises}'));return b
  end
end
