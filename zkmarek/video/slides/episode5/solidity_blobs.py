from manim import (DOWN, FadeIn, Write, Indicate, Scene, Text, PINK, TEAL_E, RIGHT, MoveToTarget, 
                   TransformMatchingShapes, LEFT, Arrow, StealthTip, GREY_A, FadeOut, GrowArrow, UP, 
                   ImageMobject, MAROON_C, Brace, Create, ORIGIN)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT2_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code
from zkmarek.video.mobjects.verkle_tree import VerkleTree
class BlobsSolidity(CodeSlide):


    def __init__(self):
        super().__init__("Blobs in Solidity", "zkmarek/video/slides/episode5/blobs.sol")

    def construct(self):
        super().construct()
        self.code.next_to(self.title_text, DOWN, buff = 0).scale(0.85)
        self.commitment = "bytes48 commitment"
        self.x = "bytes32 x"
        self.y = "bytes32 y"
        self.proof = "bytes48 proof"
        self.blobIndex = "uint256 blobIndex"
        
        self.input_data = "bytes memory data = abi.encodePacked(commitment, x, y, proof);"

        self.precompile = "data.verifyKZGProof()"
        
        self.success = "require(data.verifyKZGProof(), 'KZG proof verification failed');"

        self.commitmentHash = "bytes32 commitmentHash"
        
        
        self.calc_hash = "bytes32 commitmentHash = sha256(abi.encodePacked(commitment));"

        
        self.blob = ImageMobject("data/images/blob.png").scale(0.5).shift(UP*0.7+LEFT*3)
        self.blobIndex_text = Text("blobIndex", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24).move_to(self.blob.get_center())
        
        self.blob_hash_text = Text("blobhash(blobIndex)", font_size= 28, font = PRIMARY_FONT).set_color(HIGHLIGHT_COLOR).next_to(self.blob, DOWN).shift(DOWN+LEFT*1)
        self.version_hash = Text("0x01 SHA-256 (KZG commitment)", font=PRIMARY_FONT, font_size=28).next_to(self.blob_hash_text, RIGHT).shift(RIGHT*2)
        self.arrow_hash_ec = Arrow(self.blob_hash_text.get_right(), self.version_hash.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY_A])
        self.version_hash_part1 = self.version_hash[0:4]
        self.version_hash_part1.set_color_by_gradient([TEAL_E, PRIMARY_COLOR])
        self.brace_version = Brace(self.version_hash_part1, DOWN).set_color(HIGHLIGHT2_COLOR)
        self.version_hash_part2 = self.version_hash[4:25]
        self.version_hash_part2.set_color(SECONDARY_COLOR)
        self.brace_hash = Brace(self.version_hash_part2, DOWN).set_color(SECONDARY_COLOR)
        self.text_version = Text("version", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        self.brace_version.put_at_tip(self.text_version)
        self.text_hash = Text("last 31 bytes", color = MAROON_C, font= PRIMARY_FONT, font_size = 24)
        self.brace_hash.put_at_tip(self.text_hash)
        
        self.commitment_real = "commitment"
        self.brace_32B = Brace(self.version_hash, DOWN, color = PRIMARY_COLOR)
        self.brace_32b_text = Text("32 bytes", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 26)
        self.brace_32B.put_at_tip(self.brace_32b_text)
        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "pseudo code: inputs", "data/sound/e5/slide6-1.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.code))
        scene.wait(7.5)
        
        self.new_subsection(scene, "commitment", "data/sound/e5/slide6-1a.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.commitment, 0, run_time=0.9, color = PINK)

        self.new_subsection(scene, "x and y", "data/sound/e5/slide6-1b.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.x, 0, run_time=0.7, color = PINK)
        self.indicate_code(scene, self.code, self.y, 0, run_time=0.7, color = PINK)
        
        self.new_subsection(scene, "proof", "data/sound/e5/slide6-1c.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.proof, 0, run_time=0.9, color = PINK)
        
        self.new_subsection(scene, "blobIndex", "data/sound/e5/slide6-1d.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.blobIndex, 0, run_time=0.9)
        scene.wait(2.3)
        
        self.new_subsection(scene, "pack into byte array", "data/sound/e5/slide6-2.mp3")
        kzg_input = [self.x, self.y, self.commitment, self.proof]
        scene.wait(1)
        for input in kzg_input:
            self.indicate_code(scene, self.code, input, 0, run_time=0.4, color = MAROON_C)
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.input_data, 0, run_time=1)
        
        self.new_subsection(scene, "bool - success", "data/sound/e5/slide6-3.mp3")
        scene.wait(1.5)
        scene.wait(1)
        self.indicate_code(scene, self.code, self.precompile, 0, run_time=0.8, color = TEAL_E)
        scene.wait(2.8)
        self.indicate_code(scene, self.code, self.success, 0, run_time=0.9)
        
        self.new_subsection(scene, "blobhash()", "data/sound/e5/slide6-4.mp3")
        scene.wait(6)
        self.indicate_code(scene, self.code, "blobhash", run_time=0.9, color = PINK)
        self.code.generate_target()
        self.code.target.scale(0.4).shift(RIGHT*3+UP)
        scene.play(MoveToTarget(self.code))
        scene.play(Write(self.blob_hash_text), FadeIn(self.blob))
        
        self.new_subsection(scene, "blobindex - 32 bytes", "data/sound/e5/slide6-4a.mp3")
        scene.wait(1.2)
        scene.play(Indicate(self.blob_hash_text[9:18], color = PINK))
        scene.play(Write(self.version_hash), GrowArrow(self.arrow_hash_ec), FadeIn(self.brace_32B, self.brace_32b_text))
        scene.wait(2.3)

        
        self.new_subsection(scene, "SHA256", "data/sound/e5/slide6-4b.mp3")
        scene.play(FadeOut(self.brace_32B, self.brace_32b_text), run_time=0.5)
        scene.play(FadeIn(self.brace_hash, self.brace_version), Write(self.text_version), Write(self.text_hash))
        scene.play(Indicate(self.text_version, color = PRIMARY_COLOR), run_time=0.7)
        scene.wait(1)
        scene.play(Indicate(self.text_hash, color = PRIMARY_COLOR))
        scene.play(Indicate(self.version_hash[4:11], color = MAROON_C))
        scene.wait(1.8)
        scene.play(FadeOut(self.blob, self.text_hash, self.text_version, self.version_hash, self.brace_hash, self.brace_version, self.arrow_hash_ec, self.blob_hash_text))
        self.code.generate_target()
        self.code.target.scale(1/0.4).next_to(self.title_text, DOWN, buff = 0).shift(DOWN*0.1)
        scene.play(MoveToTarget(self.code))
        scene.wait(0.2)

        scene.wait(1.5)
        
        
        self.new_subsection(scene, "verifyBlobHash", "data/sound/e5/slide6-5.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.calc_hash, 0, run_time=0.9, color = TEAL_E)
        scene.wait(2.4)
        
        self.new_subsection(scene, "last 31 bytes", "data/sound/e5/slide6-6.mp3")
        scene.wait(1)

        self.indicate_code(scene, self.code, "uint256(blobHash) & ((1 << 248) - 1) == uint256(commitmentHash) & ((1 << 248) - 1)", 0, run_time=0.9, color = TEAL_E)
        scene.wait(3)
        
        self.new_subsection(scene, "congratulations", "data/sound/e5/slide6-7.mp3")
        scene.wait(3)
        
        self.summary(scene)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_tezt_summary))
        
    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=0.5, color = SECONDARY_COLOR):
        chars = find_in_code(code, fragment)
        scene.play(Indicate(chars[index], color=color, scale_factor=1.05), run_time=run_time)
    
    def summary(self, scene):
        self.new_subsection(scene, "summary", "data/sound/e5/slide6-8.mp3")
        self.title_tezt_summary = Text("Up next...", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP).shift(DOWN*0.5)
        self.blob.move_to(ORIGIN)
        self.blob1 = self.blob.copy().scale(0.5).next_to(self.blob, RIGHT, buff = 0)
        self.blob2 = self.blob.copy().scale(0.5).next_to(self.blob, LEFT, buff = 0)
        scene.play(TransformMatchingShapes(self.title_text, self.title_tezt_summary), FadeOut(self.code))
        scene.play(FadeIn(self.blob))

        tree = VerkleTree().scale(0.7).shift(UP)
        scene.play(FadeIn(self.blob1), run_time=0.5)
        scene.play(FadeIn(self.blob2), run_time=0.5)
        scene.wait(4.5)
        scene.play(FadeOut(self.blob, self.blob1, self.blob2), run_time=0.5)
        scene.play(Create(tree), run_time=2)
        scene.wait(1)
        scene.play(FadeOut(tree))
        
